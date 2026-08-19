import asyncio
import httpx

# เปลี่ยน IP ตรงนี้ให้เป็น IP เครื่องที่เป็น Server
# - หากทดสอบบนเครื่องตัวเองคนเดียว ให้ใช้ "127.0.0.1"
# - หากทดสอบกับเพื่อนในวง LAN ให้ใส่ IP เครื่อง Server เช่น "172.20.57.24"
# SERVER_IP = "10.141.0.1"
SERVER_IP = "10.170.62.211"

PORT = "8088"
SERVER_URL = f"http://{SERVER_IP}:{PORT}"

# ระบุรหัสนักเรียนของผู้ส่ง
MY_STUDENT_ID = "6710301007"


async def send_claim_request(client: httpx.AsyncClient, req_id: int):
    """ส่งคำขอเคลมคูปอง 1 ครั้ง"""
    try:
        res = await client.post(
            f"{SERVER_URL}/claim",
            json={"student_id": MY_STUDENT_ID},
            timeout=5.0,
        )
        data = res.json()
        status = data.get("status")
        msg = data.get("message", data.get("claimed_coupon"))
        print(f" -- คำขอที่ #{req_id}: [{status}] -> {msg}")
        return status
    except Exception as e:
        print(f" -- คำขอที่ #{req_id} เกิดข้อผิดพลาด: {e}")
        return "ERROR"


async def hunt_coupons():
    async with httpx.AsyncClient() as client:
        print(f"[{MY_STUDENT_ID}] เริ่มต้นภารกิจแย่งชิงคูปอง (Concurrent Requests)...")

        # ส่งคำขอเคลมคูปองพร้อมกันหลายคำขอ (Concurrent)
        tasks = [send_claim_request(client, i) for i in range(1, 4)]
        await asyncio.gather(*tasks)

        # ----------------------------------------------------
        # 1. ดึงสรุปคูปองส่วนตัว (เฉพาะของ MY_STUDENT_ID)
        # ----------------------------------------------------
        print("\nกำลังดึงสรุปคูปองของตนเอง...")
        try:
            res = await client.get(f"{SERVER_URL}/my-coupons/{MY_STUDENT_ID}")
            if res.status_code == 200:
                summary = res.json()
                total = summary.get("total_claimed", 0)
                coupons = summary.get("claimed_coupons", [])
                print(
                    f"สรุปผลส่วนตัว [{MY_STUDENT_ID}]: ได้รับคูปองรวม {total} ใบ -> {coupons}"
                )
            else:
                print(
                    f"ดึงข้อมูลส่วนตัวไม่สำเร็จ Status Code: {res.status_code}"
                )
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการดึงข้อมูลส่วนตัว: {e}")

        # ----------------------------------------------------
        # 2. ดึงสรุปภาพรวมทั้งหมดของกลุ่ม (จาก Server /summary)
        # ----------------------------------------------------
        print("\n" + "=" * 60)
        print("📊 สรุปผลการแจกคูปองของทุกคนในกลุ่ม")
        print("=" * 60)
        try:
            res = await client.get(f"{SERVER_URL}/summary")
            if res.status_code == 200:
                summary_data = res.json()
                remaining_stock = summary_data.get("remaining_stock", 0)
                student_claims = summary_data.get("student_claims", {})

                one_coupon_students = []
                two_coupon_students = []
                zero_coupon_students = []

                for student, coupons in student_claims.items():
                    count = len(coupons)
                    print(
                        f" - นักเรียน [{student}]: ได้ {count} ใบ -> {coupons}"
                    )
                    if count == 1:
                        one_coupon_students.append(student)
                    elif count == 2:
                        two_coupon_students.append(student)
                    elif count == 0:
                        zero_coupon_students.append(student)

                print("-" * 60)
                print(f"📦 คูปองคงเหลือในคลัง Server: {remaining_stock} ใบ")
                print(
                    f"🏆 คนที่ได้ครบ 2 ใบ ({len(two_coupon_students)} คน): {two_coupon_students}"
                )
                if one_coupon_students:
                    print(
                        f"⚠️ คนที่ได้เพียง 1 ใบ ({len(one_coupon_students)} คน): {one_coupon_students}"
                    )
                if zero_coupon_students:
                    print(
                        f"❌ คนที่ไม่ได้คูปองเลย ({len(zero_coupon_students)} คน): {zero_coupon_students}"
                    )
                print("=" * 60)
            else:
                print(
                    f"ดึงข้อมูลสรุปกลุ่มไม่สำเร็จ Status Code: {res.status_code}"
                )
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการดึงสรุปกลุ่ม: {e}")


if __name__ == "__main__":
    asyncio.run(hunt_coupons())
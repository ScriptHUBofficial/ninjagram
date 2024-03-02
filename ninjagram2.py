from instagrapi import Client

try:
    # Instagram hesap bilgilerinizi buraya girin
    ACCOUNT_USERNAME = "scriptbullet"
    ACCOUNT_PASSWORD = "12345678"

    cl = Client()
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

    # Takip etmek istediğiniz hesabın kullanıcı adını belirtin
    target_account_username = "scriptbullet"

    # Takip etme işlemi
    target_user_id = cl.user_id_from_username(target_account_username)
    cl.user_follow(target_user_id)

    print(f"{target_account_username} hesabı takip edildi.")

except Exception as e:
    print(f"Hata: {e}")


from instagrapi import Client

try:
    SESSION_COOKIE = "kuuki"

    cl = Client()
    cl.session_id = SESSION_COOKIE

    # Takip etmek istediğiniz hesabın kullanıcı adını belirtin
    target_account_username = "scriptbullet"

    target_user_id = cl.user_id_from_username(target_account_username)
    cl.user_follow(target_user_id)

    print(f"{target_account_username} hesap takip edildi.")

except Exception as e:
    print(f"Hata: {e}")

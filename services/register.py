import firebase_admin
from firebase_admin import credentials, auth, db

cred = credentials.Certificate('srt-rsrv-firebase-adminsdk.json')

# Firebase 앱 초기화
firebase_admin.initialize_app(cred)

try:
    # 사용자 등록
    user = auth.create_user(
        email=user_email,
        password=user_password
    )
    print(f"User {user.email} created with UID: {user.uid}")
except Exception as e:
    print(f"Error creating user: {e}")
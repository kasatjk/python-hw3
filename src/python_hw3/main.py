from .auth.account import Account

def main() -> None:
    acc1 = Account('user1', 'email@email.com', 'Password123')
    
    acc1.display_info()
    acc1.verify_password('abcd')
    acc1.verify_password('12345678')
    acc1.update_email('email@email.new')
    try:
        acc1.change_password('00000000', 'abcdefgh')
    except ValueError as e:
        print(f"Expected error: {e}")
    acc1.change_password('Password123', 'NewPassword456')
    acc1.display_info()

if __name__ == "__main__":
    main()

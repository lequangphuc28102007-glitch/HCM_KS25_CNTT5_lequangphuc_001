from database import PlayerManager
from models import Player
import utils

def main():
    while True:
        manager = PlayerManager()
        print("\n=== Menu ===")
        print("1.hiển thị danh sách cầu thủ")
        print("2.thêm cầu thủ mới")
        print("3.cập nhật thông tin cầu thủ")
        print("4.xóa cầu thủ")
        print("5.tìm kiếm cầu thủ")
        print("6.thoát")

        choice = input("hãy nhập vào lựa chọn:")

        match choice:
            case "1":
                if not manager.players:
                    print("danh sách đang trống")
                    continue
                else:
                    utils.show_all(manager.players)
            case "2":
                print("\n=== thêm cầu thủ mới ==")
                player_id = input("hãy nhập vào mã cầu thủ:")
                player_name = input("hãy nhập tên cầu thủ:")
                speed_score = int(input("hãy nhập vào điểm tốc độ:"))
                technique_score = int(input("hãy nhập vào điểm kĩ thuật:"))
                goal_score = int(input("hãy nhập vào điểm ghi bàn:"))
                
                
                new_player = Player(player_id, player_name, speed_score, technique_score, goal_score)
                manager.players.append(new_player)
                Player.update_status_player(new_player)


                print("đã thêm thành công cầu thủ!")

            case "3":
                player_id = input("hãy nhập vào mã cầu thủ:")
                if not player_id:
                    print("không tìm thấy cầu thủ cần cập nhật!")
                else:
                    new_speed = input("hãy nhập vào tốc độ mới!")
                    new_technique = input("hãy nhập vào kĩ thuật:")
                    new_goal = input("hãy nhập vào ghi bàn:")


            case "4":
                player_id = input("hãy nhập vào cầu thủ muốn xóa:")

                confirm = input("bạn có muốn xóa cầu thủ này hay không(y-n):")

                if confirm.lower() == "y":
                    manager.delete_player(player_id)
                    print("đã xóa thành công")

                else:
                    print("đã hủy thao tác xóa")

            case "5":
                print("\n=== tìm kiếm cầu thủ ===")
                keyword = input("hãy nhập vào tên cầu thủ muốn tìm:")
                result = manager.search_player(keyword)
                if not result:
                    print("không tìm thấy cầu thủ phù hợp")
                else:
                    print("đã tìm thấy các cầu thủ phù hợp")
                    utils.show_all(result)

            case "6":
                print("cảm ơn bạn đã sử dụng hệ thống quản lí bóng đá!")
                break
            case _:
                print("lựa chọn không hợp lệ! vui lòng nhập từ 1 - 6!")

if __name__ == "__main__":
    main()
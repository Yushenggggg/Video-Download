from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from pytube import YouTube
import instaloader
import yt_dlp
import requests
from bs4 import BeautifulSoup
from io import BytesIO
import os


# 創建主窗口
root = tk.Tk()
root.title("影片下載器")

# 設置窗口大小
window_width = 445
window_height = 180
# 獲取屏幕的寬度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# 計算窗口左上角的位置，使其居中顯示
x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)
# 設置窗口大小和位置
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# 禁用窗口大小調整
root.resizable(False, False)

# 定義變數：下載路徑
download_path = tk.StringVar()

# 定義函數：選擇下載路徑
def select_download_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        download_path.set(folder_selected)
        return True
    return False

# 定義函數：下載YouTube影片
def download_youtube_video():
    if not select_download_folder():
        return
    url = entry_url.get()
    if not url:
        messagebox.showerror("錯誤", "請提供有效的YouTube影片URL")
        return
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{download_path.get()}/%(title)s.%(ext)s',
            'ffmpeg_location': 'C:/ffmpeg/ffmpeg-7.0.2-full_build/bin'  # 替換為實際的ffmpeg路徑
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("成功", "YouTube影片下載成功！")
    except Exception as e:
        messagebox.showerror("錯誤", f"下載失敗: {e}")

# 定義函數：下載YouTube影片並轉換為MP3
def download_youtube_to_mp3():
    if not select_download_folder():
        return
    url = entry_url.get()
    if not url:
        messagebox.showerror("錯誤", "請提供有效的YouTube影片URL")
        return
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{download_path.get()}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': 'C:/ffmpeg/ffmpeg-7.0.2-full_build/bin'  # 替換為實際的ffmpeg路徑
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("成功", "YouTube影片已成功轉換為MP3格式！")
    except Exception as e:
        messagebox.showerror("錯誤", f"下載或轉換失敗: {e}")


# 定義函數：下載Instagram影片
def download_instagram_video():
    if not select_download_folder():
        return
    url = entry_url.get()
    if not url:
        messagebox.showerror("錯誤", "請提供有效的Instagram影片URL")
        return
    try:
        L = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])
        L.download_post(post, target=download_path.get())
        messagebox.showinfo("成功", "Instagram 影片下載成功！")
    except Exception as e:
        messagebox.showerror("錯誤", f"下載失敗: {e}")

# 定義函數：下載Facebook影片
def download_facebook_video():
    if not select_download_folder():
        return
    url = entry_url.get()
    if not url:
        messagebox.showerror("錯誤", "請提供有效的Facebook影片URL")
        return
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{download_path.get()}/%(title)s.%(ext)s',
            'ffmpeg_location': 'C:/ffmpeg/ffmpeg-7.0.2-full_build/bin'  # 替換為實際的ffmpeg路徑
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("成功", "Facebook影片下載成功！")
    except Exception as e:
        messagebox.showerror("錯誤", f"下載失敗: {e}")

# 定義函數：下載抖音影片
def download_tiktok_video():
    if not select_download_folder():
        return
    url = entry_url.get()
    if not url:
        messagebox.showerror("錯誤", "請提供有效的抖音影片URL")
        return
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{download_path.get()}/%(title)s.%(ext)s',
            'ffmpeg_location': 'C:/ffmpeg/ffmpeg-7.0.2-full_build/bin'  # 替換為實際的ffmpeg路徑
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("成功", "抖音影片下載成功！")
    except Exception as e:
        messagebox.showerror("錯誤", f"下載失敗: {e}")

# 定義函數：下載他人的Instagram限時動態
def download_instagram_story():
    # 創建登錄窗口
    login_window = tk.Toplevel(root)
    login_window.title("登入")
    login_window.geometry(f"350x150+{x_position+50}+{y_position}")
    login_window.resizable(False, False)

    # login_window 視窗置頂
    login_window.transient(root)
    login_window.grab_set()

    tk.Label(login_window, text="Instagram 用戶名:").grid(row=0, column=0, padx=10, pady=5)
    username_entry = tk.Entry(login_window, width=30)
    username_entry.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(login_window, text="Instagram 密碼:").grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(login_window, width=30, show='*')
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(login_window, text="2階段驗證碼 (如果有):").grid(row=2, column=0, padx=10, pady=5)
    two_factor_entry = tk.Entry(login_window, width=30)
    two_factor_entry.grid(row=2, column=1, padx=10, pady=5)

    def perform_login():
        your_username = username_entry.get()
        your_password = password_entry.get()
        two_factor_code = two_factor_entry.get()
        
        if not your_username or not your_password:
            messagebox.showerror("錯誤", "請提供有效的Instagram用戶名和密碼")
            return
        
        if not select_download_folder():
            return

        try:
            L = instaloader.Instaloader()
            L.login(your_username, your_password)  # 登錄到Instagram
            
            # 嘗試登錄，可能需要兩階段驗證
            try:
                L.login(your_username, your_password)
            except instaloader.exceptions.TwoFactorAuthRequiredException:
                if not two_factor_code:
                    messagebox.showerror("錯誤", "需要兩階段驗證碼")
                    return
                L.two_factor_login(two_factor_code)
            
            target_username = entry_url.get().split('/')[-1]  # 獲取目標用戶名
            profile = instaloader.Profile.from_username(L.context, target_username)
            
            # 下載該用戶的限時動態
            for story in L.get_stories(userids=[profile.userid]):
                for item in story.get_items():
                    L.download_storyitem(item, target=download_path.get())
            
            messagebox.showinfo("成功", f"{target_username}的限時動態下載成功！")
        except instaloader.exceptions.InstaloaderException as e:
            messagebox.showerror("錯誤", f"Instagram錯誤: {str(e)}")
        except Exception as e:
            messagebox.showerror("錯誤", f"下載失敗: {str(e)}")
        finally:
            login_window.destroy()
    
    # 創建登錄按鈕
    tk.Button(login_window, text="登入並下載", command=perform_login).grid(row=3, columnspan=2, pady=20)
    login_window.mainloop()

# 定義函數：下載Twitter影片
def download_twitter_video():
    if not select_download_folder():
        return
    url = entry_url.get()
    if not url:
        messagebox.showerror("錯誤", "請提供有效的Twitter影片URL")
        return
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{download_path.get()}/%(title)s.%(ext)s',
            'ffmpeg_location': 'C:/ffmpeg/ffmpeg-7.0.2-full_build/bin'  # 替換為實際的ffmpeg路徑
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("成功", "Twitter影片下載成功！")
    except Exception as e:
        messagebox.showerror("錯誤", f"下載失敗: {e}")

# 定義函數：下載LINE貼圖並轉換為透明背景PNG
def download_line_stickers():
    if not select_download_folder():
        return
    
    url = entry_url.get()  # 從輸入框獲取LINE貼圖URL
    if not url:
        messagebox.showerror("錯誤", "請提供有效的LINE貼圖URL")
        return

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        sticker_images = soup.find_all('img', class_='FnStickerPreviewItem')

        # 創建存儲資料夾
        download_folder = download_path.get()
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        
        for i, img in enumerate(sticker_images):
            img_url = img['src']
            img_response = requests.get(img_url)
            img_data = Image.open(BytesIO(img_response.content))
            img_data = img_data.convert("RGBA")  # 轉換為RGBA模式

            datas = img_data.getdata()
            new_data = []
            for item in datas:
                # 移除白色背景，並將其設置為透明
                if item[0] == 255 and item[1] == 255 and item[2] == 255:
                    new_data.append((255, 255, 255, 0))
                else:
                    new_data.append(item)

            img_data.putdata(new_data)
            img_data.save(f"{download_folder}/sticker_{i + 1}.png")

        messagebox.showinfo("成功", "LINE貼圖下載並已轉換為透明背景PNG格式！")
    
    except Exception as e:
        messagebox.showerror("錯誤", f"下載或處理失敗: {e}")

path = "image/"
# 打開和調整圖標大小
youtube_image = Image.open(path + "youtube.png")
youtube_image = youtube_image.resize((32, 32), Image.Resampling.LANCZOS)  # 調整到32x32像素
youtube_icon = ImageTk.PhotoImage(youtube_image)

instagram_image = Image.open(path +"instagram.png")
instagram_image = instagram_image.resize((32, 32), Image.Resampling.LANCZOS)
instagram_icon = ImageTk.PhotoImage(instagram_image)

facebook_image = Image.open(path + "facebook.png")
facebook_image = facebook_image.resize((32, 32), Image.Resampling.LANCZOS)
facebook_icon = ImageTk.PhotoImage(facebook_image)

tiktok_image = Image.open(path + "tiktok.png")
tiktok_image = tiktok_image.resize((32, 32), Image.Resampling.LANCZOS)
tiktok_icon = ImageTk.PhotoImage(tiktok_image)

music_image = Image.open(path +"music.png")
music_image = music_image.resize((32, 32), Image.Resampling.LANCZOS)  # 調整到32x32像素
music_icon = ImageTk.PhotoImage(music_image)

story_image = Image.open(path +"instagram.png")
story_image = story_image.resize((32, 32), Image.Resampling.LANCZOS)
story_icon = ImageTk.PhotoImage(story_image)

# 為Twitter按鈕添加圖標
twitter_image = Image.open(path + "twitter.png")
twitter_image = twitter_image.resize((32, 32), Image.Resampling.LANCZOS)
twitter_icon = ImageTk.PhotoImage(twitter_image)

# 創建輸入URL的文本框
entry_url = tk.Entry(root, width=60)
entry_url.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

# YT影片
btn_download_youtube = tk.Button(root, image=youtube_icon, command=download_youtube_video)
btn_download_youtube.grid(row=2, column=0, padx=3, pady=3)
# IG影片
btn_download_instagram = tk.Button(root, image=instagram_icon, command=download_instagram_video)
btn_download_instagram.grid(row=2, column=1, padx=3, pady=3)
# FB影片
btn_download_facebook = tk.Button(root, image=facebook_icon, command=download_facebook_video)
btn_download_facebook.grid(row=2, column=2, padx=3, pady=3)

# YT音樂
btn_download_youtube = tk.Button(root, image=music_icon, command=download_youtube_to_mp3)
btn_download_youtube.grid(row=3, column=0, padx=3, pady=3)
# IG限時
btn_download_instagram = tk.Button(root, text="IG限時", command=download_instagram_story)
btn_download_instagram.grid(row=3, column=1, padx=3, pady=3)
# 抖音
btn_download_tiktok = tk.Button(root, image=tiktok_icon, command=download_tiktok_video)
btn_download_tiktok.grid(row=3, column=2, padx=3, pady=3)

# 在主窗口中添加Twitter下載按鈕
btn_download_twitter = tk.Button(root, image=twitter_icon, command=download_twitter_video)
btn_download_twitter.grid(row=4, column=0, padx=3, pady=3)

# LINE圖標
line_image = Image.open(path + "line.png")
line_image = line_image.resize((32, 32), Image.Resampling.LANCZOS)
line_icon = ImageTk.PhotoImage(line_image)

# 添加LINE貼圖下載按鈕
btn_download_line = tk.Button(root, image=line_icon, command=download_line_stickers)
btn_download_line.grid(row=4, column=1, padx=3, pady=3)




# 運行主循環
root.mainloop()

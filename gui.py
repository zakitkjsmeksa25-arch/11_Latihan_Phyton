import customtkinter as ctk
import math
import gspread
from google.oauth2.service_account import Credentials

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# ==========================================
# KONEKSI GOOGLE SHEETS & FUNGSI DATABASE
# ==========================================
def hubung_database():
    try:
        scope = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = Credentials.from_service_account_file("credentials.json", scopes=scope)
        client = gspread.authorize(creds)
        sheet = client.open("database").sheet1
        
        if sheet.cell(1, 1).value == "":
            sheet.update("A1:B1", [["username", "password"]])
        return sheet
    except Exception as e:
        print("Gagal terhubung ke Google Sheets:", e)
        return None

sheet_db = hubung_database()

# ==========================================
# FUNGSI MODUL KAMU
# ==========================================
# Modul 1: Geometri
def luas_segiempat(s): return s * s
def keliling_segiempat(s): return 4 * s
def luas_bundaran(r): return 3.14 * r * r
def luas_tiga_sisi(a, t): return 0.5 * a * t

# Modul 2: Logika
def apakah_prima(n):
    if n <= 1: return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0: return False
    return True

def cek_ganjil_genap(x):
    return "Genap" if x % 2 == 0 else "Ganjil"


# ==========================================
# GUI UTAMA APLIKASI
# ==========================================
class AppUtama(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Aplikasi Matematika & Logika")
        self.geometry("750x500")

        # Layout Grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ---------------- Halaman Login / Registrasi ----------------
        self.frame_auth = ctk.CTkFrame(self, corner_radius=15)
        self.frame_auth.pack(expand=True, fill="both", padx=40, pady=40)

        self.lbl_auth = ctk.CTkLabel(self.frame_auth, text="Masuk ke Aplikasi", font=ctk.CTkFont(size=24, weight="bold"))
        self.lbl_auth.pack(pady=(30, 20))

        self.entry_user = ctk.CTkEntry(self.frame_auth, placeholder_text="Username", width=250)
        self.entry_user.pack(pady=10)

        self.entry_pass = ctk.CTkEntry(self.frame_auth, placeholder_text="Password", show="*", width=250)
        self.entry_pass.pack(pady=10)

        self.btn_login = ctk.CTkButton(self.frame_auth, text="Login", width=250, command=self.proses_login)
        self.btn_login.pack(pady=10)

        self.btn_register = ctk.CTkButton(self.frame_auth, text="Buat Akun Baru", fg_color="transparent", border_width=1, width=250, command=self.proses_daftar)
        self.btn_register.pack(pady=5)

        self.lbl_status_auth = ctk.CTkLabel(self.frame_auth, text="", font=ctk.CTkFont(size=14))
        self.lbl_status_auth.pack(pady=10)

        # Container Dashboard (Disembunyikan saat awal)
        self.frame_dashboard = ctk.CTkFrame(self, fg_color="transparent")

    # ---------------- Logika Auth ----------------
    def proses_login(self):
        user = self.entry_user.get().strip()
        pwd = self.entry_pass.get().strip()

        if not sheet_db:
            self.lbl_status_auth.configure(text="Gagal terhubung ke database!", text_color="#E74C3C")
            return

        data = sheet_db.get_all_values()
        for baris in data[1:]:
            if len(baris) >= 2 and baris[0] == user and baris[1] == pwd:
                self.frame_auth.pack_forget()
                self.buka_dashboard(user)
                return

        self.lbl_status_auth.configure(text="Username atau password salah!", text_color="#E74C3C")

    def proses_daftar(self):
        user = self.entry_user.get().strip()
        pwd = self.entry_pass.get().strip()

        if not user or not pwd:
            self.lbl_status_auth.configure(text="Isi username & password!", text_color="#E74C3C")
            return

        if not sheet_db:
            self.lbl_status_auth.configure(text="Gagal terhubung ke database!", text_color="#E74C3C")
            return

        data = sheet_db.get_all_values()
        for baris in data[1:]:
            if len(baris) >= 1 and baris[0] == user:
                self.lbl_status_auth.configure(text="Username sudah digunakan!", text_color="#E74C3C")
                return

        sheet_db.append_row([user, pwd])
        self.lbl_status_auth.configure(text="Akun berhasil dibuat! Silakan Login.", text_color="#2FA572")

    # ---------------- Dashboard Setelah Login ----------------
    def buka_dashboard(self, username):
        self.frame_dashboard.pack(expand=True, fill="both")
        self.frame_dashboard.grid_columnconfigure(1, weight=1)
        self.frame_dashboard.grid_rowconfigure(0, weight=1)

        # Sidebar Navigasi
        sidebar = ctk.CTkFrame(self.frame_dashboard, width=180, corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="nsew")

        lbl_welcome = ctk.CTkLabel(sidebar, text=f"Halo,\n{username}!", font=ctk.CTkFont(size=18, weight="bold"))
        lbl_welcome.pack(padx=20, pady=(20, 20))

        btn_geo = ctk.CTkButton(sidebar, text="Modul Geometri", command=self.tampil_geometri)
        btn_geo.pack(padx=15, pady=8)

        btn_log = ctk.CTkButton(sidebar, text="Modul Logika", fg_color="transparent", border_width=1, command=self.tampil_logika)
        btn_log.pack(padx=15, pady=8)

        switch_theme = ctk.CTkSwitch(sidebar, text="Dark Mode", command=self.toggle_theme)
        switch_theme.pack(side="bottom", padx=15, pady=20)
        switch_theme.select()

        # Layar Konten Utama
        self.konten = ctk.CTkFrame(self.frame_dashboard, corner_radius=10)
        self.konten.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.tampil_geometri()

    def bersihkan_konten(self):
        for widget in self.konten.winfo_children():
            widget.destroy()

    # ---------------- Halaman Modul Geometri ----------------
    def tampil_geometri(self):
        self.bersihkan_konten()

        title = ctk.CTkLabel(self.konten, text="Kalkulator Geometri", font=ctk.CTkFont(size=22, weight="bold"))
        title.pack(anchor="w", padx=20, pady=(15, 10))

        # Input Sisi Segiempat
        card1 = ctk.CTkFrame(self.konten, corner_radius=10)
        card1.pack(fill="x", padx=20, pady=10, ipady=5)

        ctk.CTkLabel(card1, text="Hitung Segiempat (Luas & Keliling)").pack(anchor="w", padx=10, pady=2)
        entry_sisi = ctk.CTkEntry(card1, placeholder_text="Masukkan panjang sisi")
        entry_sisi.pack(fill="x", padx=10, pady=5)
        
        lbl_res_geo = ctk.CTkLabel(card1, text="", font=ctk.CTkFont(weight="bold"))
        lbl_res_geo.pack(pady=2)

        def hitung_segiempat():
            v = entry_sisi.get().strip()
            if v.replace('.', '', 1).isdigit():
                s = float(v)
                lbl_res_geo.configure(text=f"Luas: {luas_segiempat(s)} | Keliling: {keliling_segiempat(s)}", text_color="#2FA572")
            else:
                lbl_res_geo.configure(text="Masukkan angka yang valid!", text_color="#E74C3C")

        ctk.CTkButton(card1, text="Hitung", fg_color="#2FA572", command=hitung_segiempat).pack(anchor="e", padx=10, pady=5)

    # ---------------- Halaman Modul Logika ----------------
    def tampil_logika(self):
        self.bersihkan_konten()

        title = ctk.CTkLabel(self.konten, text="Modul Logika & Bilangan", font=ctk.CTkFont(size=22, weight="bold"))
        title.pack(anchor="w", padx=20, pady=(15, 10))

        card = ctk.CTkFrame(self.konten, corner_radius=10)
        card.pack(fill="x", padx=20, pady=10, ipady=5)

        ctk.CTkLabel(card, text="Cek Ganjil/Genap & Bilangan Prima").pack(anchor="w", padx=10, pady=2)
        entry_angka = ctk.CTkEntry(card, placeholder_text="Masukkan angka bulat")
        entry_angka.pack(fill="x", padx=10, pady=5)

        lbl_res_logika = ctk.CTkLabel(card, text="", font=ctk.CTkFont(weight="bold"))
        lbl_res_logika.pack(pady=5)

        def proses_logika():
            v = entry_angka.get().strip()
            if v.isdigit():
                n = int(v)
                gg = cek_ganjil_genap(n)
                pr = "Prima" if apakah_prima(n) else "Bukan Prima"
                lbl_res_logika.configure(text=f"Angka {n}: Bilangan {gg} & {pr}", text_color="#3B82F6")
            else:
                lbl_res_logika.configure(text="Masukkan angka bulat positif!", text_color="#E74C3C")

        ctk.CTkButton(card, text="Cek Angka", command=proses_logika).pack(anchor="e", padx=10, pady=5)

    def toggle_theme(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")


if __name__ == "__main__":
    app = AppUtama()
    app.mainloop()
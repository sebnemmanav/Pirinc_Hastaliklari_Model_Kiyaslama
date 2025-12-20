from google.colab import userdata, drive
import os
import json

def initialize_and_download():
    """
    Drive'ı bağlar, Kaggle API'yi kurar ve eksik veri setlerini indirir.
    """
    # 1. Drive Bağlantısı
    if not os.path.exists('/content/drive'):
        drive.mount('/content/drive')

    # 2. Secrets'tan Bilgileri Çek
    K_USER = userdata.get('KAGGLE_USERNAME')
    K_KEY = userdata.get('KAGGLE_KEY')
    D_PATH = userdata.get("DATA_PATH")

    if not K_USER or not K_KEY:
        print("HATA: Kaggle bilgileri Secrets'ta (Asma Kilit) bulunamadı!")
        return

    # 3. Kaggle API Yapılandırması
    os.environ['KAGGLE_USERNAME'] = str(K_USER)
    os.environ['KAGGLE_KEY'] = str(K_KEY)
    
    kaggle_dir = os.path.expanduser("~/.kaggle")
    os.makedirs(kaggle_dir, exist_ok=True)
    with open(os.path.join(kaggle_dir, 'kaggle.json'), 'w') as f:
        json.dump({'username': K_USER, 'key': K_KEY}, f)
    os.chmod(os.path.join(kaggle_dir, 'kaggle.json'), 0o600)
    
    print("Kaggle API başarıyla yapılandırıldı.")

    # 4. Veri Setlerini Kontrol Et ve İndir
    os.makedirs(D_PATH, exist_ok=True)

    # --- PADDY DOCTOR ---
    p_folder = os.path.join(D_PATH, "paddy_doctor")
    p_zip = os.path.join(D_PATH, "paddy-disease-classification.zip")
    
    if not os.path.exists(p_folder) or not os.listdir(p_folder):
        print("-> Paddy Doctor indiriliyor...")
        os.system(f'kaggle competitions download -c paddy-disease-classification -p "{D_PATH}"')
        if os.path.exists(p_zip):
            os.system(f'unzip -q "{p_zip}" -d "{p_folder}"')
            os.system(f'rm "{p_zip}"')
            print("Paddy Doctor başarıyla indirildi.")
    else:
        print("Paddy Doctor zaten mevcut.")

    # --- RICE LEAF DISEASES ---
    r_folder = os.path.join(D_PATH, "rice_diseases_lab")
    if not os.path.exists(r_folder) or not os.listdir(r_folder):
        print("-> Rice Leaf Diseases indiriliyor...")
        os.system(f'kaggle datasets download -d vbookshelf/rice-leaf-diseases --unzip -p "{r_folder}"')
        print("Rice Leaf Diseases başarıyla indirildi.")
    else:
        print("Rice Leaf Diseases zaten mevcut.")

    print("\nSistem hazır ve tüm veri setleri kontrol edildi.")

    
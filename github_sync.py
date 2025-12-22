import os
import subprocess

def sync(commit_message="Kod güvenliği sağlandı ve yollar gizlendi"):
    project_dir = os.getcwd() 
    
    try:
        subprocess.run(["git", "add", "*.py", "*.ipynb", ".gitignore"], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], capture_output=True)
        subprocess.run(["git", "push", "-f", "origin", "master"], check=True)
        print("\n Güvenli senkronizasyon tamamlandı!")
    except Exception as e:
        print(f" Hata: {e}")

if __name__ == '__main__':
    sync()
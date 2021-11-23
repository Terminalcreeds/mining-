import sys
import os



def mining():
	while True:
		print("------ Mining on Windows Linux run only on linux--------")
		print("""
	[*] Start Mining
	[*] Download Ubuntu for Windows
	[*] Install 
	[*] About
	[*] Help


			""")
		command = str(input(">>> "))

		if command == "d":
			get = str(input("Are you sure you want to download ubuntu Y/N: "))
			if get == "Y" or get == "y":
				os.system("start ms-windows-store:")
			else:
				new =input("Start Mining? Y/N: ")
				if new == "y":
					print("Please wait a sec...")
					os.system("sudo apt install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev -y")
					try:
						os.system("git clone https://github.com/xmrig/xmrig.git")
					except Exception:
						print("git not install")
						install = str(input("Install?: Y/N"))
						if install == "Y":
							os.system("apt-get install git")
						else:
							break
						


					#os.system("sudo apt install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev -y")



if __name__ == "__main__":
	mining()


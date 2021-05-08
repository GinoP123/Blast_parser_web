import os


def reset():
	for file in os.listdir("/tmp/"):
		if file.endswith(".xlsx") or file.endswith(".txt"):
			os.remove(f"/tmp/{file}")

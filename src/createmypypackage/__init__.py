import os
import subprocess
import tempfile

def exec(x):
    subprocess.check_output(x,shell=True)


def create_package():
    file_path=os.path.abspath(input("Give python file location where all functions and import statements are written please: ").strip())
    if(input("Will you like to add more python files which are imported by the main file? Yes/No:").lower().strip()=="yes"):
        extra_file_paths=[i for i in input("Give the location of extra_files seperated by space").split() if(i!="")]
    else:
        extra_file_paths=[]
    with tempfile.TemporaryDirectory() as tmpdirname:
        os.chdir(tmpdirname)
        exec("git clone https://github.com/Souvic/package_creator.git")
        exec("rm -rf ./package_creator/.git")

        package_name=input("Choose name of this package please: ")
        author_name=input("Author's name please: ")
        author_email=input("Author's EmailId please: ")

        python_requires=input("Required minimum Python version to run this package please(e.g. 3.6): ")

        rep_url=input("Go to github.com, create an empty repository with project name, copy-paste the link here please: ")
        if(not rep_url.lower().endswith(".git")):
            rep_url=rep_url+".git"
        with open("./package_creator/src/package_name/__init__.py","w") as f:
            f.write(open(file_path,"r").read())
        exec("pipreqs ./package_creator/")
        print("install_requires in setup.cfg is filled up with minimum requirements from pipreqs package")
        print("Feel free to change setup.cfg after this in your github repo directly in case of different versions to be used")
        with open("./package_creator/requirements.txt") as f:
            install_requires="".join(["\n\t"+i for i in f.read().replace("==",">=").split("\n")])
    
        with open("./package_creator/setup.cfg","r") as f:
            su=f.read()
        su=su.format(package_name=package_name,author_name=author_name,author_email=author_email,python_requires=python_requires,install_requires=install_requires,rep_url=rep_url)
        with open("./package_creator/setup.cfg","w") as f:
            f.write(su)
        for ii in extra_file_paths:
            exec(f"cp {ii} ./package_creator/src/package_name/")
        os.rename("./package_creator/src/package_name","./package_creator/src/"+package_name)
        
        #exec("python3 -m twine upload --repository testpypi")
        os.chdir("./package_creator/")
        exec("python3 -m build")
        exec("git init")
        exec("git add -A")
        #exec("git add .")
        exec("git commit -m 'First commit in the new package'")
        print("Uploading to github")
        print("Get ready with your github username and passtoken")
        exec("git branch -M main")
        exec(f"git remote add origin {rep_url}")
        exec("git push -u origin main")
        print("Done!!")
        print("All set up!!")
     
    
def uploadpackage():
    with tempfile.TemporaryDirectory() as tmpdirname:
        os.chdir(tmpdirname)
        rep_url=input("Copy-paste the link of the github repo of the project please: ")
        if(not rep_url.lower().endswith(".git")):
            rep_url=rep_url+".git"
        exec(f"git clone {rep_url}")
        dir_ = [i for i in os.listdir() if os.path.isdir(i)][0]
        os.chdir(dir_)
        exec(f"rm -rf ./dist")
        nft_=input("Are you uploading this package to PyPi for the first time? Yes/No:").lower().strip()=="no"
        if(nft_):
            with open("./setup.cfg","r") as f:
                zz=f.read().split("\n")
            if(zz[2].startswith("version")):
                kindex=2
            else:
                for jkl in range(len(zz)):
                    if(zz[jkl].startswith("version")):
                        kindex=jkl
                        break;
                    
            
            print(f"The old {zz[kindex]}")
            new_version_number=input("Choose a new version number: ")
            zz[kindex]="version = "+new_version_number
            with open("./setup.cfg","w") as f:
                f.write("\n".join(zz))
        exec("python3 -m build")
        exec("git add -A")
        exec("git commit -m 'First commit in the new package'")
        if(nft_):
            exec(f"git tag v{new_version_number}")
            exec(f"git push origin  v{new_version_number}")
        else:
            exec("git tag v0.0.1")
            exec("git push origin  v0.0.1")
        exec("git push -u origin main")
        print("Updated github repo!")
        exec("twine upload dist/*")
        print("Updated to PyPi!")
        
if(input("Do you already have a github repo for the project? Yes/No:").lower().strip()=="yes"):
    uploadpackage()
else:
    create_package()
        
    
       

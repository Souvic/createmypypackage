import os
import tempfile

file_path=os.path.abspath(input("Give python file location where all functions and import statements are written please: ").strip())
if(input("Will you like to add more python files which are imported by the main file? Yes/No:").lower().strip()=="yes"):
    extra_file_paths=[i for i in input("Give the location of extra_files seperated by space").split() if(i!="")]
else:
    extra_file_paths=[]
with tempfile.TemporaryDirectory() as tmpdirname:
    os.chdir(tmpdirname)
    os.system("git clone https://github.com/Souvic/package_creator.git")
    os.system("rm -rf ./package_creator/.git")

    package_name=input("Choose name of this package please: ")
    author_name=input("Author's name please: ")
    author_email=input("Author's EmailId please: ")

    python_requires=input("Required minimum Python version to run this package please(e.g. 3.6): ")

    rep_url=input("Go to github.com, create an empty repository with project name, copy-paste the link here please: ")
    if(not rep_url.lower().endswith(".git")):
        rep_url=rep_url+".git"
    with open("./package_creator/src/package_name/__init__.py","w") as f:
        f.write(open(file_path,"r").read())
    os.system("pipreqs ./package_creator/")
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
        os.system(f"cp {ii} ./package_creator/src/package_name/")
    os.rename("./package_creator/src/package_name","./package_creator/src/"+package_name)
    
    #os.system("python3 -m twine upload --repository testpypi")
    os.chdir("./package_creator/")
    os.system("python3 -m build")
    os.system("git init")
    os.system("git add -A")
    #os.system("git add .")
    os.system("git commit -m 'First commit in the new package'")
    print("Uploading to github")
    print("Get ready with your github username and passtoken")
    os.system("git branch -M main")
    os.system(f"git remote add origin {rep_url}")
    os.system("git push -u origin main")
    print("Done!!")
    print("All set up!!")
    
       

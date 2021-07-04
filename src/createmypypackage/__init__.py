import os
import tempfile

def exec(x):
    if os.system(x)!=0:
        raise NameError('Look at above errors to understand why the execution failed!!')
        
def check_(prompt_,yes_="yes",no_="no"):
    yes1_=yes_.lower().strip()
    no1_=no_.lower().strip()
    while(True):
        i_=input(prompt_).lower().strip()
        if(i_==yes1_):
            return(True)
        elif(i_==no1_):
            return(False)
        else:
            print(f"Your input is neither {yes_} nor {no_}. TRY again carefully..")
        
def format_readme(rep_u):
    #https://github.com/{user_name_}/{repo_or_package_name_}.git
    user_name_=rep_u.split("/")[-2]
    repo_or_package_name_=rep_u.split("/")[-1][:-4]
    with open("./package_creator/README.md","r") as f:
        readme=f.read()
    readme=readme.format(user_name_=user_name_,repo_or_package_name_=repo_or_package_name_)
    with open("./package_creator/README.md","w") as f:
        f.write(readme)
    
def create_package():
    file_path=os.path.abspath(os.path.expanduser(input("Give python file location where all functions and import statements are written please: ").strip()))
    if(check_("Will you like to add more python files which are imported by the main file? yes/no: ")):
        extra_file_paths=set([os.path.abspath(os.path.expanduser(i)) for i in input("Give the location of extra_files seperated by space : ").split() if(i!="")])
    else:
        extra_file_paths=[]
    with tempfile.TemporaryDirectory() as tmpdirname:
        os.chdir(tmpdirname)
        exec("git clone -q https://github.com/Souvic/package_creator.git")
        exec("rm -rf ./package_creator/.git")

        package_name=input("Choose name of this package please: ")
        author_name=input("Author's name please: ")
        author_email=input("Author's EmailId please: ")

        python_requires=input("Required minimum Python version to run this package please(e.g. 3.6): ")

        rep_url=input("Go to github.com, create an empty repository(without any file) with project name, copy-paste the link here please: ")
        if(not rep_url.lower().endswith(".git")):
            rep_url=rep_url+".git"
        format_readme(rep_url)
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
        print(f"\n\n\n__________________________\nYou may now go to {rep_url[:-4]} and change atleast README.MD and description in setup.cfg")
        print("You may require to also change requirements.txt and install_requires,python_requires on setup.cfg if you feel so")
        print("To upload to PyPI and reflect the new changes, run this command(cmpp) once again! This time you already have a github repo.")
     
    
def uploadpackage():
    with tempfile.TemporaryDirectory() as tmpdirname:
        os.chdir(tmpdirname)
        rep_url=input("Copy-paste the link of the github repo of the project please: ")
        if(not rep_url.lower().endswith(".git")):
            rep_url=rep_url+".git"
        exec(f"git clone -q {rep_url}")
        dir_ = [i for i in os.listdir() if os.path.isdir(i)][0]
        os.chdir(dir_)
        exec(f"rm -rf ./dist")
        
        print("\n\n\n_____________________________IMPORTANT________________________________\n\nYour package requires atleast these packages listed in requirements.txt and install_requires part of setup.cfg file.")
        print("These are listed by pipreqs")
        exec("pipreqs --print ./")
        print("\n\nThese are the packages listed in requirements.txt : ")
        exec("cat requirements.txt")
        tempprint=""
        print("\n\nThese are the packages listed in install_requires part of setup.cfg file : ")
        with open("setup.cfg","r") as f:
            flag=False
            for j in f:
                if(not j[0].isspace()):
                    flag=False
                if(flag):
                    tempprint+=j.strip()+"\n"
                if(j.startswith("install_requires")):
                   flag=True
        
        
        print(tempprint)
        print("If you notice any discrepency, abort now and update requirements.txt setup.cfg file(install_requires and python_requires).\n")
        if(check_("Abort/continue? (see above why..) Write 'abort' to stop exeution or 'continue' to go ahead uploading with current settings : ","abort","continue")):
            raise NameError('Aborted as you wished!! \nMake necessary changes on the repo now.')
        nft_=check_("Are you uploading this package to PyPi for the first time? yes/no: ","no","yes")
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
        exec("git commit -m 'New version is released now'")
        if(nft_):
            exec(f"git tag v{new_version_number}")
            exec(f"git push origin  v{new_version_number}")
        else:
            exec("git tag v0.0.1")
            exec("git push origin  v0.0.1")
        exec("git push -u origin main")
        print("Updated github repo!")
        exec("twine upload dist/*")
        print("Updated to PyPi! New version has been released!")
        
        
def main():
    if(check_("Have you already uploaded the project once to github repo ? yes/no: ")):
        uploadpackage()
    else:
        create_package()
        
    
       

# utgår helt och hållet från (men skapar virtual env först https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/ ) https://www.youtube.com/watch?v=dam0GPOAvVI

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=8000)
    


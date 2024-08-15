from appConfig import AppConfig

if __name__ == '__main__':
    app = AppConfig()
    app.SetupFrames()
    app.SetupTextos()
    app.SetupBotoes()
    app.SetupLogos()

    app.master.mainloop()
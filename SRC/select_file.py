import PySimpleGUI as sg
def get_file():
    GUI_rows = [[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
                 [sg.InputText(), sg.FileBrowse()],
                 [sg.Submit(), sg.Cancel()]]

    (button, (source_filename,)) = sg.Window('SHA-1 & 256 Hash').Layout(GUI_rows).Read()
    #print(button, source_filename)
    return(button, source_filename)
if __name__=="__main__":
    get_file()
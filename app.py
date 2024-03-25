from models.email_client.email_parser import Email_Parser
from models import email
from models.utils import utils
from vue.mainPage import MailListWidget
from controller.MailListWidgetController import MailListWidgetController
from PyQt5.QtWidgets import QApplication,QDialog
from models.DB.SQliteDAO import SQLiteDAO
from vue.loginPage import PasswordInputDialog
import sys

if __name__ == "__main__":
    # Création de l'application
    app = QApplication(sys.argv)

    # Création de la boîte de dialogue pour le mot de passe
    dialog = PasswordInputDialog()

    # Affichage de la boîte de dialogue et récupération du résultat
    result = dialog.exec_()

    # Vérification si un mot de passe a été fourni
    if result == QDialog.Accepted:
        # Récupération du mot de passe
        password = dialog.password

        # Initialisation de la base de données avec le mot de passe
        bdd = SQLiteDAO("models/DB/database.db", password)

        # Création du contrôleur
        mail_list_controller = MailListWidgetController(bdd)

        # Création de la fenêtre principale et affichage
        window = MailListWidget(mail_list_controller)
        window.show()

        # Exécution de l'application
        app.exec_()



    #gmail
    #mailparser = Email_Parser("imap.gmail.com","julienvacher44@gmail.com","azph qifg xunl elxw")
    #orange
    #mailparser = Email_Parser("imap.orange.fr","julien.vacher2@orange.fr","temporarymdpJUJU44521")
    #outlook
    #mailparser = Email_Parser("imap-mail.outlook.com","julien.vacher2@outlook.fr","G6;=(\N|@>~@*INl")
    #gmail
    #tangjuyo44@gmail.com ynxg qtaf dlpp ryln
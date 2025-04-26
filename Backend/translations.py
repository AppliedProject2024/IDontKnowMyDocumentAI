import streamlit as st

#dictionary of translations for application text
translations = {

    "error_uploading_file": {
        "English": "Error uploading file.",
        "Spanish": "Error al subir el archivo.",
        "French": "Erreur lors du téléchargement du fichier.",
        "Portuguese": "Erro ao carregar o arquivo.",
        "German": "Fehler beim Hochladen der Datei."
    },

    "file_already_uploaded": {
        "English": "File has already been uploaded.",
        "Spanish": "El archivo ya ha sido subido.",
        "French": "Le fichier a déjà été téléchargé.",
        "Portuguese": "O arquivo já foi carregado.",
        "German": "Die Datei wurde bereits hochgeladen."
    },

    "login_success": {
        "English": "Login Successful!",
        "Spanish": "¡Inicio de sesión exitoso!",
        "French": "Connexion réussie !",
        "Portuguese": "Login bem-sucedido!",
        "German": "Anmeldung erfolgreich!"
    },

    "login_failed": {
        "English": "Login failed.",
        "Spanish": "Error al iniciar sesión.",
        "French": "Échec de la connexion.",
        "Portuguese": "Falha no login.",
        "German": "Anmeldung fehlgeschlagen."
    },

    "email_not_verified": {
        "English": "Email not verified. Please check your email for a verification link.",
        "Spanish": "Correo electrónico no verificado. Por favor, revise su correo para el enlace de verificación.",
        "French": "Email non vérifié. Veuillez vérifier votre email pour le lien de vérification.",
        "Portuguese": "Email não verificado. Por favor, verifique seu email para o link de verificação.",
        "German": "E-Mail nicht verifiziert. Bitte überprüfen Sie Ihre E-Mail für einen Bestätigungslink."
    },

    "server_connection_error": {
        "English": "Error connecting to server.",
        "Spanish": "Error al conectar con el servidor.",
        "French": "Erreur de connexion au serveur.",
        "Portuguese": "Erro ao conectar ao servidor.",
        "German": "Fehler bei der Verbindung zum Server."
    },

    "registration_failed": {
        "English": "Registration failed. Please try again.",
        "Spanish": "Error en el registro. Por favor, inténtelo de nuevo.",
        "French": "Échec de l'inscription. Veuillez réessayer.",
        "Portuguese": "Falha no registro. Por favor, tente novamente.",
        "German": "Registrierung fehlgeschlagen. Bitte versuchen Sie es erneut."
    },

    "registration_success": {
        "English": "Registration successful! Please check your email for a verification link.",
        "Spanish": "¡Registro exitoso! Por favor, revise su correo electrónico para encontrar el enlace de verificación.",
        "French": "Inscription réussie ! Veuillez vérifier votre email pour le lien de vérification.",
        "Portuguese": "Registro bem-sucedido! Por favor, verifique seu email para o link de verificação.",
        "German": "Registrierung erfolgreich! Bitte überprüfen Sie Ihre E-Mail für einen Bestätigungslink."
    },

    "enter_valid_credentials": {
        "English": "Please enter a valid email and password.",
        "Spanish": "Por favor, introduce un correo electrónico y contraseña válidos.",
        "French": "Veuillez entrer un email et un mot de passe valides.",
        "Portuguese": "Por favor, insira um email e senha válidos.",
        "German": "Bitte geben Sie eine gültige E-Mail-Adresse und ein Passwort ein."
    },

    "session_expired": {
        "English": "Session expired. Please login again.",
        "Spanish": "Sesión expirada. Por favor, inicie sesión de nuevo.",
        "French": "Session expirée. Veuillez vous reconnecter.",
        "Portuguese": "Sessão expirada. Por favor, faça login novamente.",
        "German": "Sitzung abgelaufen. Bitte melden Sie sich erneut an."
    },

    "app_title": {
        "English": "🤖 StudyBuddy AI",
        "Spanish": "🤖 StudyBuddy IA",
        "French": "🤖 StudyBuddy IA",
        "Portuguese": "🤖 StudyBuddy IA",
        "German": "🤖 StudyBuddy KI"
    },
    
    #main page
    "chat_placeholder": {
        "English": "Enter your question...",
        "Spanish": "Escribe tu pregunta...",
        "French": "Entrez votre question...",
        "Portuguese": "Digite sua pergunta...",
        "German": "Gib deine Frage ein..."
    },
    "thinking": {
        "English": "Thinking...",
        "Spanish": "Pensando...",
        "French": "Réflexion...",
        "Portuguese": "Pensando...",
        "German": "Denken..."
    },
    
    #auth pages
    "login_header": {
        "English": "Login",
        "Spanish": "Iniciar Sesión",
        "French": "Connexion",
        "Portuguese": "Entrar",
        "German": "Anmelden"
    },
    "register_header": {
        "English": "Register",
        "Spanish": "Registrarse",
        "French": "S'inscrire",
        "Portuguese": "Registrar",
        "German": "Registrieren"
    },
    "email_label": {
        "English": "Email",
        "Spanish": "Correo electrónico",
        "French": "Email",
        "Portuguese": "Email",
        "German": "E-Mail"
    },
    "password_label": {
        "English": "Password",
        "Spanish": "Contraseña",
        "French": "Mot de passe",
        "Portuguese": "Senha",
        "German": "Passwort"
    },
    "login_button": {
        "English": "Login",
        "Spanish": "Iniciar Sesión",
        "French": "Connexion",
        "Portuguese": "Entrar",
        "German": "Anmelden"
    },
    "register_button": {
        "English": "Register",
        "Spanish": "Registrarse",
        "French": "S'inscrire",
        "Portuguese": "Registrar",
        "German": "Registrieren"
    },

    "institutional_email_warning": {
        "English": "Warning: Due to institutional filtering, student email accounts may not receive the verification email. Please consider signing up with a Gmail account to ensure you receive the email.",
        "Spanish": "Advertencia: Debido al filtrado institucional, es posible que las cuentas de correo electrónico de estudiantes no reciban el correo de verificación. Considere registrarse con una cuenta de Gmail para asegurarse de recibir el correo.",
        "French": "Avertissement : En raison du filtrage institutionnel, les comptes e-mail étudiants peuvent ne pas recevoir l'e-mail de vérification. Veuillez envisager de vous inscrire avec un compte Gmail pour vous assurer de recevoir l'e-mail.",
        "Portuguese": "Aviso: Devido a filtragem institucional, contas de e-mail estudantis podem não receber o e-mail de verificação. Por favor, considere se registrar com uma conta Gmail para garantir que você receba o e-mail.",
        "German": "Warnung: Aufgrund institutioneller Filterung erhalten studentische E-Mail-Konten möglicherweise keine Bestätigungs-E-Mail. Bitte erwägen Sie die Anmeldung mit einem Gmail-Konto, um sicherzustellen, dass Sie die E-Mail erhalten."
    },

    "logged_in_as": {
        "English": "Logged in as:",
        "Spanish": "Conectado como:",
        "French": "Connecté en tant que:",
        "Portuguese": "Conectado como:",
        "German": "Angemeldet als:"
    },
    "logout_button": {
        "English": "Logout",
        "Spanish": "Cerrar sesión",
        "French": "Déconnexion",
        "Portuguese": "Sair",
        "German": "Abmelden"
    },
    "login_required": {
        "English": "Please login to access the application",
        "Spanish": "Por favor inicia sesión para acceder a la aplicación",
        "French": "Veuillez vous connecter pour accéder à l'application",
        "Portuguese": "Por favor, faça login para acessar o aplicativo",
        "German": "Bitte melden Sie sich an, um auf die Anwendung zuzugreifen"
    },

    "already_logged_in": {
       "English": "You are already logged in. Logging in with a new account will log you out!",
       "Spanish": "Ya has iniciado sesión. ¡Iniciar sesión con una nueva cuenta cerrará tu sesión actual!",
       "French": "Vous êtes déjà connecté. La connexion avec un nouveau compte vous déconnectera !",
       "Portuguese": "Você já está logado. Fazer login com uma nova conta fará com que você seja desconectado!",
       "German": "Sie sind bereits angemeldet. Die Anmeldung mit einem neuen Konto meldet Sie ab!"
   },
    
    #summary page
    "summary_header": {
        "English": "📚Summary",
        "Spanish": "📚Resumen",
        "French": "📚Résumé",
        "Portuguese": "📚Resumo",
        "German": "📚Zusammenfassung"
    },
    "enter_query_summary": {
        "English": "Enter query for summarisation",
        "Spanish": "Ingresa consulta para resumir",
        "French": "Entrez une requête pour le résumé",
        "Portuguese": "Digite consulta para resumo",
        "German": "Anfrage für Zusammenfassung eingeben"
    },
    "select_word_count": {
        "English": "Select number of words",
        "Spanish": "Selecciona número de palabras",
        "French": "Sélectionnez le nombre de mots",
        "Portuguese": "Selecione o número de palavras",
        "German": "Wortanzahl auswählen"
    },
    "select_complexity": {
        "English": "Select complexity",
        "Spanish": "Selecciona complejidad",
        "French": "Sélectionnez la complexité",
        "Portuguese": "Selecione a complexidade",
        "German": "Komplexität auswählen"
    },
    "complexity_low": {
        "English": "low",
        "Spanish": "baja",
        "French": "faible",
        "Portuguese": "baixa",
        "German": "niedrig"
    },
    "complexity_medium": {
        "English": "medium",
        "Spanish": "media",
        "French": "moyenne",
        "Portuguese": "média",
        "German": "mittel"
    },
    "complexity_high": {
        "English": "high",
        "Spanish": "alta",
        "French": "élevée",
        "Portuguese": "alta",
        "German": "hoch"
    },
    "get_summary_button": {
        "English": "Get Summary",
        "Spanish": "Obtener Resumen",
        "French": "Obtenir le Résumé",
        "Portuguese": "Obter Resumo",
        "German": "Zusammenfassung abrufen"
    },
    "enter_all_fields": {
        "English": "Please enter a query, word count and complexity.",
        "Spanish": "Por favor, ingresa una consulta, recuento de palabras y complejidad.",
        "French": "Veuillez entrer une requête, un nombre de mots et une complexité.",
        "Portuguese": "Por favor, insira uma consulta, contagem de palavras e complexidade.",
        "German": "Bitte geben Sie eine Anfrage, Wortanzahl und Komplexität ein."
    },
    
    #MCQ page
    "mcq_header": {
        "English": "✔️MCQ",
        "Spanish": "✔️Preguntas",
        "French": "✔️QCM",
        "Portuguese": "✔️Questões",
        "German": "✔️Multiple-Choice"
    },
    "enter_query_mcq": {
        "English": "Enter query for MCQ",
        "Spanish": "Ingresa consulta para preguntas",
        "French": "Entrez une requête pour QCM",
        "Portuguese": "Digite consulta para questões",
        "German": "Anfrage für Multiple-Choice eingeben"
    },
    "number_of_questions": {
        "English": "Number of questions",
        "Spanish": "Número de preguntas",
        "French": "Nombre de questions",
        "Portuguese": "Número de perguntas",
        "German": "Anzahl der Fragen"
    },
    "complexity_level": {
        "English": "Complexity level",
        "Spanish": "Nivel de complejidad",
        "French": "Niveau de complexité",
        "Portuguese": "Nível de complexidade",
        "German": "Komplexitätsniveau"
    },
    "create_mcq_button": {
        "English": "Create MCQ",
        "Spanish": "Crear Preguntas",
        "French": "Créer QCM",
        "Portuguese": "Criar Questões",
        "German": "Multiple-Choice erstellen"
    },
    "please_enter_query": {
        "English": "Please enter a query.",
        "Spanish": "Por favor, ingresa una consulta.",
        "French": "Veuillez entrer une requête.",
        "Portuguese": "Por favor, insira uma consulta.",
        "German": "Bitte geben Sie eine Anfrage ein."
    },
    "quiz_results": {
        "English": "Quiz Results",
        "Spanish": "Resultados del Cuestionario",
        "French": "Résultats du Quiz",
        "Portuguese": "Resultados do Questionário",
        "German": "Quizergebnisse"
    },
    "your_score": {
        "English": "Your score: ",
        "Spanish": "Tu puntuación: ",
        "French": "Votre score: ",
        "Portuguese": "Sua pontuação: ",
        "German": "Ihre Punktzahl: "
    },
    "question_review": {
        "English": "Question Review",
        "Spanish": "Revisión de Preguntas",
        "French": "Révision des Questions",
        "Portuguese": "Revisão de Perguntas",
        "German": "Fragenüberprüfung"
    },

    "question": {
        "English": "Question ",
        "Spanish": "Pregunta ",
        "French": "Question",
        "Portuguese": "Pergunta",
        "German": "Frage"
    },

    "of": {
        "English": "of ",
        "Spanish": "de ",
        "French": "sur ",
        "Portuguese": "de ",
        "German": "von "
    },

    "correct_answer": {
        "English": "is the correct answer!",
        "Spanish": "es la respuesta correcta!",
        "French": "est la bonne réponse !",
        "Portuguese": "é a resposta correta!",
        "German": "ist die richtige Antwort!"
    },

    "incorrect_answer": {
        "English": "The correct answer is",
        "Spanish": "La respuesta correcta es",
        "French": "La bonne réponse est",
        "Portuguese": "A resposta correta é",
        "German": "Die richtige Antwort ist"
    },

    "previous": {
        "English": "Previous",
        "Spanish": "Anterior",
        "French": "Précédent",
        "Portuguese": "Anterior",
        "German": "Zurück"
    },
    "next": {
        "English": "Next",
        "Spanish": "Siguiente",
        "French": "Suivant",
        "Portuguese": "Próximo",
        "German": "Weiter"
    },
    "skip": {
        "English": "Skip",
        "Spanish": "Omitir",
        "French": "Passer",
        "Portuguese": "Pular",
        "German": "Überspringen"
    },
    "show_results": {
        "English": "Show Results",
        "Spanish": "Mostrar Resultados",
        "French": "Afficher les Résultats",
        "Portuguese": "Mostrar Resultados",
        "German": "Ergebnisse anzeigen"
    },
    
    #upload Page
    "upload_header": {
        "English": "Upload Your Documents",
        "Spanish": "Sube tus Documentos",
        "French": "Téléchargez vos Documents",
        "Portuguese": "Carregar seus Documentos",
        "German": "Laden Sie Ihre Dokumente hoch"
    },
    "upload_instruction": {
        "English": "Upload one PDF file",
        "Spanish": "Sube un archivo PDF",
        "French": "Téléchargez un fichier PDF",
        "Portuguese": "Carregar um arquivo PDF",
        "German": "Laden Sie eine PDF-Datei hoch"
    },
    "uploaded_files": {
        "English": "Uploaded Files",
        "Spanish": "Archivos Subidos",
        "French": "Fichiers Téléchargés",
        "Portuguese": "Arquivos Carregados",
        "German": "Hochgeladene Dateien"
    },
    "upload_success": {
        "English": " uploaded successfully!",
        "Spanish": " subido con éxito!",
        "French": " téléchargé avec succès !",
        "Portuguese": " carregado com sucesso!",
        "German": " erfolgreich hochgeladen!"
    },
    "processing_file": {
        "English": "Processing ",
        "Spanish": "Procesando ",
        "French": "Traitement de ",
        "Portuguese": "Processando ",
        "German": "Verarbeitung von "
    },
    "processing_success": {
        "English": " processed successfully!",
        "Spanish": " procesado con éxito!",
        "French": " traité avec succès !",
        "Portuguese": " processado com sucesso!",
        "German": " erfolgreich verarbeitet!"
    },
    "processing_error": {
        "English": "Error processing ",
        "Spanish": "Error al procesar ",
        "French": "Erreur lors du traitement de ",
        "Portuguese": "Erro ao processar ",
        "German": "Fehler bei der Verarbeitung von "
    },

    "file_naming_tip": {
       "English": "Tip: Use descriptive file names - you can search for content in specific files by including the file name in your query",
       "Spanish": "Consejo: Utilice nombres de archivo descriptivos - puede buscar contenido en archivos específicos incluyendo el nombre del archivo en su consulta",
       "French": "Conseil: Utilisez des noms de fichiers descriptifs - vous pouvez rechercher du contenu dans des fichiers spécifiques en incluant le nom du fichier dans votre requête",
       "Portuguese": "Dica: Use nomes de arquivos descritivos - você pode pesquisar conteúdo em arquivos específicos incluindo o nome do arquivo em sua consulta",
       "German": "Tipp: Verwenden Sie aussagekräftige Dateinamen - Sie können nach Inhalten in bestimmten Dateien suchen, indem Sie den Dateinamen in Ihre Suchanfrage einbeziehen"
   },
    
    #documents Page
    "documents_header": {
        "English": "Your Documents",
        "Spanish": "Tus Documentos",
        "French": "Vos Documents",
        "Portuguese": "Seus Documentos",
        "German": "Ihre Dokumente"
    },
    "delete_button": {
        "English": "Delete",
        "Spanish": "Eliminar",
        "French": "Supprimer",
        "Portuguese": "Excluir",
        "German": "Löschen"
    },
    "deleting_file": {
        "English": "Deleting '{filename}'...",
        "Spanish": "Eliminando '{filename}'...",
        "French": "Suppression de '{filename}'...",
        "Portuguese": "Excluindo '{filename}'...",
        "German": "Löschen von '{filename}'..."
    },
    "no_documents": {
        "English": "No documents uploaded yet.",
        "Spanish": "Aún no se han subido documentos.",
        "French": "Aucun document n'a encore été téléchargé.",
        "Portuguese": "Nenhum documento carregado ainda.",
        "German": "Noch keine Dokumente hochgeladen."
    },
    
    #feedback Page
    "feedback_header": {
        "English": "Provide Feedback",
        "Spanish": "Proporcionar Comentarios",
        "French": "Fournir des Commentaires",
        "Portuguese": "Fornecer Feedback",
        "German": "Feedback geben"
    },
    "feedback_type_label": {
        "English": "What would you like to give feedback on?",
        "Spanish": "¿Sobre qué te gustaría dar comentarios?",
        "French": "Sur quoi souhaitez-vous donner votre avis ?",
        "Portuguese": "Sobre o que você gostaria de dar feedback?",
        "German": "Worüber möchten Sie Feedback geben?"
    },
    "feedback_translation": {
        "English": "Translation",
        "Spanish": "Traducción",
        "French": "Traduction",
        "Portuguese": "Tradução",
        "German": "Übersetzung"
    },
    "feedback_qa": {
        "English": "Q&A",
        "Spanish": "Preguntas y Respuestas",
        "French": "Q&R",
        "Portuguese": "Perguntas e Respostas",
        "German": "Fragen & Antworten"
    },
    "feedback_summarisation": {
        "English": "Summarisation",
        "Spanish": "Resumen",
        "French": "Résumé",
        "Portuguese": "Resumo",
        "German": "Zusammenfassung"
    },
    "feedback_mcq": {
        "English": "MCQ",
        "Spanish": "Preguntas de Opción Múltiple",
        "French": "QCM",
        "Portuguese": "Questões de Múltipla Escolha",
        "German": "Multiple-Choice-Fragen"
    },
    "feedback_text_label": {
        "English": "Write your feedback here:",
        "Spanish": "Escribe tu comentario aquí:",
        "French": "Écrivez vos commentaires ici :",
        "Portuguese": "Escreva seu feedback aqui:",
        "German": "Schreiben Sie Ihr Feedback hier:"
    },
    "submit_button": {
        "English": "Submit Feedback",
        "Spanish": "Enviar Comentarios",
        "French": "Soumettre les Commentaires",
        "Portuguese": "Enviar Feedback",
        "German": "Feedback absenden"
    },
    "feedback_thank_you": {
        "English": "Thank you for your feedback!",
        "Spanish": "¡Gracias por tus comentarios!",
        "French": "Merci pour vos commentaires !",
        "Portuguese": "Obrigado pelo seu feedback!",
        "German": "Vielen Dank für Ihr Feedback!"
    },
    
    #language selection
    "language_label": {
        "English": "Language",
        "Spanish": "Idioma",
        "French": "Langue",
        "Portuguese": "Idioma",
        "German": "Sprache"
    }
}

#fuction to retrieve text based on language
def get_text(key, language="English"):
    #check if there is a key in the translations dictionary
    if key in translations and language in translations[key]:
        #return tranlation for the key and language
        return translations[key][language]
    return key

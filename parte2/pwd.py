#Cargamos una instancia de Console.
console = System.console()
#pedimos el pwd
pwdChar01 = console.readPassword("%s", ["Inserte el password:"])
pwdString01 = "".join(pwdChar01)
#pedimos nuevamente el pwd
pwdChar02 = console.readPassword("%s", ["Inserte nuevamente el password:"])
pwdString02 = "".join(pwdChar02)
#evaluamos que sea el mismo pwd
if (pwdString01==pwdString02):
    print 'Passwords coinciden. Puede continuar.'
else:
    print 'Passwords no coinciden. Intentelo nuevamente'
#terminamos el ejemplo
print 'Fin del ejemplo'

import os
print('Hello. Welcome to the Aidan Lybrary of Information')
print('If you are new here please type help into the console.')
commandloop = True
while commandloop == True:
  print(' ')
  command = input('AidanDatabase: ')
  if command == ("help"):
    print('the commands available for use in this console are: "help" "add data" "index data" "clear" "bash"')
  if command == ('add data'):
    addinfo = input('what do you want to add to the database: ')
    os.system('echo "" >> main.py')
    os.system('echo "    print()" >> main.py')
    os.system('echo "    print(' + "'" + addinfo + "')" + '" >> main.py')
  if command == ('clear'):
    os.system('clear')
  if command == ('bash'):
    bash_command_loop = True
    while bash_command_loop == True:
      bash_command = input("bash: ")
      os.system(bash_command)
  if command == ('index data'):
    print('here is a list of information added to the database: ')

# Asher
Asher is an AI. He can talk to you like a normal
human, learn from you, and even do tasks for you.

## Installing.
`sh -c "$(curl -fsSL https://raw.githubusercontent.com/crazywolf/Ai-Setup/master/Start.sh)"`
After that... just let it run.
Q: What about windows?
A: If you are on windows... well, install linux :)

## Running.
`bash Start.sh`
Q: Isnt this the same file as the installer?
A: Well yeah, we are awesome in that way.

## Usage.
Asher can be used for a wide range of usages.

## Modding.
1: Go to root directory in computer.
- MAC: command + shift + G ... type `~/` ... press enter
- LINUX: Go to file manager. Click `Home`
2: Enter Asher Folder...
3: Read docs on what each part does.

## Adding commands that Asher knows.
```python
if statement == 'clear':            # What Asher needs to hear to proccess the command.
    system('clear')                 # Command or other proccess to complete.
    sam_print("no.")                # What you want Asher to say when doing the command.
    return IS_COMMAND               # So the system knows that this is a command and not a normal conversation.
elif statement == 'soemthing':      # Next command incase you have heaps to add.
    #...                            # Command
    return IS_COMMAND               # To say that this is a command
return NOT_COMMAND                  # Anything not listed is not a command. (REQUIRED)
```

## Docs.
Docs are located at `https://crazywolf.github.io/Asher`

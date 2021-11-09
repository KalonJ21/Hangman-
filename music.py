import replit, sys
from replit import audio
from terminaltables import AsciiTable






def list_playing():
    playing = audio.get_playing()

    paused = audio.get_paused()

    if len(playing) == 0:
        print('No playing sources.')
    else:
        data = [['ID', 'Volume', 'File', 'Remaining Loops', 'Time Remaining']]

        for p in playing:
            data.append([
                p.id, p.volume, p.path, p.loops_remaining,
                f"{p.remaining.total_seconds()}s"
            ])
        print(AsciiTable(data, 'Playing Sources').table)
    print('')
    if len(paused) == 0:
        print('No paused sources.')
    else:
        data = [['ID', 'Volume', 'File', 'Remaining Loops', 'Time Remaining']]

        for p in paused:
            data.append([
                p.id, p.volume, p.path, p.loops_remaining,
                f"{p.remaining.total_seconds()}s"
            ])

        print(AsciiTable(data, 'Paused Sources').table)


def print_help():
    print('a file.<wav|aiff> [volume] [loopcount]: Add a file to sources.')

    print()

    print('la: List all sources.')

    print()

    print('p id: Resumes / pauses a source.')

    print()

    print('v id vol: Set the volume of a source.')

    print()

    print('l id count: Set remaining repeats of a song. Set to 0 for none.')

    print()

    print('c: Clear the console.')


def add(args):
    try:
        if len(args) == 3:
            audio.play_file(args[0], float(args[1]), True, int(args[2]))
        elif len(args) == 2:
            audio.play_file(args[0], float(args[1]))
        elif len(args) == 1:
            print('e', args[0])
            audio.play_file(args[0])
        else:
            print('You need to provide a file!')
    except FileNotFoundError:
        print(f'Could not find {args[0]}')


def pause(args):
    if len(args) != 1:
        print('You need to provide an id for the source!')
        return

    source = audio.get_source(args[0])

    if not source:
        print('Invalid source!')
        return
    source = audio.get_source(int(args[0]))

    source.toggle_playing()


def volume(args):
    if len(args) < 2:
        print('You need to provide a source id and volume level.')
        return

    source = audio.get_source(args[0])
    if not source:
        print(f'Source with id {args[0]} not found.')
        return
    source = audio.get_source(int(args[0]))
    source.volume = float(args[1])


def loop(args):
    if len(args) != 2:
        print('You need to provide a source id and loop count.')
        return

    source = audio.get_source(args[0])
    if not source:
        print(f'Source with id {args[0]} not found.')
        return
    source = audio.get_source(int(args[0]))
    source.set_loop(True, int(args[1]))


while True:

    sources = audio.get_sources()
    playing = audio.get_playing()

    print('What would you like to do?')
    print(f'There is {len(playing)} source(s) playing.	{len(sources)} total.')
    print('Enter h for help.')

    resp = input('>').lower()
    data = resp.split(' ')
    cmd = data[0]
    args = data[1:]

    if cmd == 'h':
        print_help()

    elif cmd == 'a':
        add(args)

    elif cmd == 'p':
        pause(args)

    elif cmd == 'v':
        volume(args)

    elif cmd == 'l':
        loop(args)

    elif cmd == 'c':
        replit.clear()

    elif cmd == 'la':
        list_playing()

    else:
        print(f'Invalid command: {cmd}.')

    print()

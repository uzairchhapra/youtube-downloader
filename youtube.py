from pytube import YouTube
import getopt, sys
from pytube.exceptions import RegexMatchError
from pytube.cli import on_progress

def progress(chunk,file_handler,bytes_remaining):
    print(chunk)

argumentList = sys.argv[1:]
options = "ha:f:"
long_options = ["help", "audio", "folder="]
audioOnly = False
urlProvided=''
path=''

try:
    arguments, values = getopt.getopt(argumentList, options, long_options)

    for currentArgument, currentValue in arguments:

        if currentArgument in ("-h", "--help"):
            print("\nDownload Video:")
            print('python youtube.py "url"\n')
            print('Download Video to Folder:')
            print('python youtube.py -f "path/to/folder" "url" \n')
            print('Download Audio to Folder:')
            print('python youtube.py -a -f "path/to/folder" "url"\n')
            sys.exit()

        elif currentArgument in ("-a", "--audio"):
            audioOnly=True

        elif currentArgument in ("-f", "--folder"):
            path = currentValue

    if len(values)!=1:
        print('Enter URL of YouTube Video in quotes.\n')
        print('Run the following command for help.')
        print('python youtube.py -h')
        sys.exit()

    urlProvided=values[0]
			
except getopt.error as err:
    print('Some Error occured!\nFollowing are examples on how to use the tool.\n')
    print("Download Video:")
    print('python youtube.py "url"\n')
    print('Download Video to Folder:')
    print('python youtube.py -f "path/to/folder" "url" \n')
    print('Download Audio to Folder:')
    print('python youtube.py -a -f "path/to/folder" "url"\n')
    sys.exit()



if urlProvided:
    try:
        yt = YouTube(urlProvided,on_progress_callback=on_progress)
        if not path:
            path='.'

        if audioOnly:
            saved=yt.streams.get_audio_only().download(output_path=path)
            print(f'Downloaded Audio and Saved here: {saved}')
        else:
            saved= yt.streams.get_highest_resolution().download(output_path=path)
            # saved= yt.streams.get_highest_resolution().on_progress(progress)
            print(f'Downloaded Video and Saved here: {saved}')

    except RegexMatchError as r:
        print(f'Incorrect YouTube URL provided: {urlProvided}')

    except OSError as o:
        print(f'{o.strerror}: {o.filename}')

    # except Exception as e:
    #     print(repr(e))
    #     print('Unknown error occured.')
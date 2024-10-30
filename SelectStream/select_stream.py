from pylsl import StreamInlet, resolve_bypred


print("Type the name of the stream:")
name = input()
print("Type the uid of the stream:")
uid = input()
print("Type the type of the stream:")
type = input()

predicate = "name='" + name + "'" and "type='" + uid + "'" and " uid='" + type + "'"
print("Finding stream...")
streams = resolve_bypred(predicate, 0, 0)
count = len(streams)
if(count == 0):
     print("No such streams were found")
elif(count == 1):
    stream = StreamInlet(streams[0])
    print("Connected to stream")
else:
    print("Multiple streams of this kind were found")
    i = 0
    for stream in streams:
        print(i, stream.name, stream.type, stream.uid, stream.channel_count)
        i += 1
    print("Choose stream (type the number)")
    choice = input()
    try:
        val = int(choice)
    except ValueError:
        print("Input is not a number")
    stream = StreamInlet(choice - 1)
    print("Connected to stream")

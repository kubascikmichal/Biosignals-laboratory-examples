from pylsl import resolve_byprop, resolve_streams
 
print("Choose stream type:")
type = input()
if type:
    print("Looking for", type, "streams...")
    streams = resolve_byprop("type", type, 0, 0.5)
else:
    print("Looking for all streams...")
    streams = resolve_streams(0.5)
 
if(len(streams) == 0):
    print("No streams were found")
else:
    print(len(streams), "were found:")
    for stream in streams:
        print(stream.name(), " ", stream.type(), " ", stream.channel_count(), " ", stream.uid())

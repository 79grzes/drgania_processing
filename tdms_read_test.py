from nptdms import TdmsFile

tdms_file = TdmsFile.read("14.03.2015.tdms")
for group in tdms_file.groups():
    group_name = group.name
    for channel in group.channels():
        channel_name = channel.name
        # Access dictionary of properties:
        properties = channel.properties
        # Access numpy array of data for channel:
        data = channel[:]
        # Access a subset of data
        data_subset = channel[10:20]
        print(data_subset)
        print("test communicate")

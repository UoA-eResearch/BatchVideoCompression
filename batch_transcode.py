#!/usr/bin/env python3

# Run this script with something like:
# nohup time python3 batch_transcode.py &> batch_transcode.log &

import ffmpeg
import os
import pandas as pd
from tqdm.auto import tqdm
from tqdm.contrib.concurrent import thread_map, process_map
import shutil
tqdm.pandas()

# Read filelist
df = pd.read_csv("reslig202200005-BestStart-EEG_recall_progress", header=None, names=["filepath"], delimiter="\t")

# Just AVI
df = df[df.filepath.str.endswith(".MOV")]

# Just get the files that are on fast tier
#df = df[df.current_size_bytes > df.actual_size_bytes]

# Sort by file size, so we do the easiest ones first
#df = df.sort_values(by="actual_size_bytes")

def set_atime(filename):
    stat = os.stat(filename)
    os.utime(filename, (1672484400, stat.st_mtime))

def transcode(input_file, dry_run=False):
    # paths look like:
    # ressci201800042-reach-raw/RAW Phase 2/084 P2/084 P2 CAM3/084 Child tasks part A CAM3.avi
    #print(input_file)
    # Replace .avi extension with .mp4
    output_file = os.path.splitext(input_file)[0] + ".mp4"
    #print("Output file:", output_file)
    if not os.path.isfile(input_file):
        # Input file moved to archive, already done
        return
    if not dry_run:
        try:
            out, err = (
                ffmpeg
                .input(input_file)
                .output(output_file, vcodec='libx264', pix_fmt='yuv420p', r=25, vb='5800K', maxrate='7800K', bufsize='2400K', bf=2, keyint_min=60, g=60, refs=4)
                .run(overwrite_output=True, quiet=True)
            )
        except ffmpeg.Error as e:
            print('stdout:', e.stdout.decode('utf8'))
            print('stderr:', e.stderr.decode('utf8'))
            return
    original_folder = os.path.dirname(input_file)
    archive_folder = original_folder.replace("reslig202200005-BestStart-EEG/", "reslig202200005-BestStart-EEG/Archive/")
    assert original_folder != archive_folder
    os.makedirs(archive_folder, exist_ok=True)
    archive_file = os.path.join(archive_folder, os.path.basename(input_file))
    #print("Archive file:", archive_file)
    if not dry_run:
        shutil.move(input_file, archive_file)
        set_atime(archive_file)


# Test on smallest file
#transcode(df[df.current_size_bytes > 10000].sort_values(by="current_size_bytes").filepath.iloc[0])
# Do it all in parallel
process_map(transcode, df.filepath, max_workers=16)#, chunksize=100)
#df.filepath.progress_apply(transcode)
print("All done!")

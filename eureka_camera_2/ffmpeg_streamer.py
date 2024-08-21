import ffmpeg
import threading
import io

in_filename = '/dev/video6' # Input file for testing (".264" or ".h264" is a convention for elementary h264 video stream file)

## Build synthetic video, for testing:
################################################
# ffmpeg -y -r 10 -f lavfi -i testsrc=size=192x108:rate=1 -c:v libx264 -crf 23 -t 50 test_vid.264

#width, height = 192, 108

#(
 #   ffmpeg
#    .input('testsrc=size={}x{}:rate=1'.format(width, height), f='lavfi')
 #   .output(in_filename, vcodec='libx264', crf=23, t=50)
 #   .overwrite_output()
 #   .run()
#)
################################################


# Use ffprobe to get video frames resolution
###############################################
# p = ffmpeg.probe(in_filename, select_streams='v');
# width = p['streams'][0]['width']
# height = p['streams'][0]['height']
###############################################


# Stream the video as array of bytes (simulate the stream from the camera for testing)
###############################################
## https://github.com/kkroening/ffmpeg-python/blob/master/examples/README.md
#sreaming_process = (
#    ffmpeg
#    .input(in_filename)
#    .video # Video only (no audio).
#    .output('pipe:', format='h264')
#    .run_async(pipe_stdout=True) # Run asynchronous, and stream to stdout
#)
###############################################


# Read from stdout in chunks of 16K bytes
def reader():
    chunk_len_in_byte = 16384  # I don't know what is the optimal chunk size
    in_bytes = chunk_len_in_byte

    # Read until number of bytes read are less than chunk_len_in_byte
    # Also stop after 10000 chucks (just for testing)
    chunks_counter = 0
    while (chunks_counter < 10000):
        in_bytes = process.stdout.read(chunk_len_in_byte) # Read 16KBytes from PIPE.
        stream.write(in_bytes) # Write data to In-memory bytes streams
        chunks_counter += 1
        if len(in_bytes) < chunk_len_in_byte:
            break


# Use public RTSP Streaming for testing
# in_stream = "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov"

# Execute ffmpeg as asynchronous sub-process.
# The input is in_filename, and the output is a PIPE.
# Note: you should replace the input from file to camera (I might forgot an argument that tells ffmpeg to expect h264 input stream).
process = (
    ffmpeg
    .input(in_filename) #.input(in_stream)
    .video
    .output('pipe:', format='h264')
    .run_async(pipe_stdin=True, pipe_stdout=True)
)

# Open In-memory bytes streams
stream = io.BytesIO()

thread = threading.Thread(target=reader)
thread.start()

# Join thread, and wait for processes to end.
thread.join()

try:
    process.wait(timeout=5)
except sp.TimeoutExpired:
    process.kill()  # Kill subprocess in case of a timeout (there might be a timeout because input stream still lives).

#sreaming_process.wait()  # sreaming_process is used 

stream.seek(0) #Seek to beginning of stream.

# Write result to "in_vid.264" file for testing (the file is playable).
print(stream.getvalue())
#with open("in_vid.264", "wb") as f:
#    f.write(stream.getvalue())
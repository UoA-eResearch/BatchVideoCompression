# BatchVideoCompression

The code in this repository is aimed at researchers at the University of Auckland (UoA) to compress video files on their existing storage infrastructure.
The code is tailored to the specific UoA research drive environment. 
Parts are inherited from [vault recall]([url](https://github.com/UoA-eResearch/vault_recall)https://github.com/UoA-eResearch/vault_recall) which makes sure that all videos on a given research drive are available for video compression (and not in ObjectStore/'Vault' subfolder or on magnetic tape/'Archive' subfolder.

## The benefits of compressed video

- fast viewing (especially if wanting to open the video on your local computer, or even an Virtual Machine (VM)). If you currently face challenges with stuttering video, compression might be a good solution
- video files maintain their location (stay in their folders), and file names are unchanged. Only the file extension (.mov, .mp4,...) might change
- original vidoe files are moved to the Archive/magnetic tape, so another backup exists
- less storage means more resources available to other researchers and less carbon footprint

## The drawback of compressing video are
- setup time and file handling (as a solution, we have created these programs/scrips/automations)
- compression time (highly CPU intense, therefore, we either provide you with a suitable VM or temporarily upgrade your existing VM)

## The prerequistes are

- get in touch with the Centre for eResearch to get an efficient overivew of how much storage space your videos on a given research drive take up
- get a sample of compressed video to gauge if these files are suitable
- a formal decision by the project's Principal Investigator (PI) station that the video compression is adequate for a given research project
- nominate a researcher/reserach supporter who supports the exection of this code


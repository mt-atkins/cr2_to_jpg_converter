# cr2_to_jpg_converter

This script an accepts input and output directory paths as arguments, and it will process all CR2 files in the input directory, saving the converted JPG files in the output directory.

To run the script using Docker, use the following command:

```shell
docker run -it -v $PWD\images:/input -v $PWD\images-out:/output cr2_to_jpg_converter-multi /input /output
```

Replace $PWD\images with the absolute path to the directory containing your CR2 files and $PWD\images-out with the absolute path to the directory where you want to save the converted JPG files.

This command will mount both input and output directories inside the container, and the script will process all CR2 files in the input directory, saving the converted JPG files in the output directory.

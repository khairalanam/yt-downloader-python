# YouTube Playlist Downloader

## Overview

Welcome to the YouTube Playlist Downloader project! This application allows users to download entire YouTube playlists seamlessly from the playlist URLs. It leverages Python, customtkinter for the GUI, and various other libraries for efficient parallel video downloads. This is a little side-project that I built to explore and learn more about parallelism and concurrency.

## Table of Contents

- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Parallelism and Concurrency](#parallelism-and-concurrency)
- [Performance Benchmarks](#performance-benchmarks)
- [Benchmark Observations](#benchmark-observations)
- [Architecture](#architecture)
- [Usage](#usage)
- [Contributions](#contributions)
- [License](#license)
- [Conclusion](#conclusion)

## Tech Stack

- **Python**: The primary programming language. (3.12 to be specific)
- **concurrent.futures**: Utilized for thread-based parallelism.
- **customtkinter**: A customized version of the Tkinter library for creating the GUI. it is basically a modern wrapper around the Tkinter library.
- **PIL (Pillow)**: Python Imaging Library, used for working with images.
- **urllib**: Library for handling URLs, employed for fetching images.
- **io**: Core module for handling I/O operations.
- **os**: Core module for interacting with the OS.

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/YouTubePlaylistDownloader.git
   ```

2. Navigate to the project directory:

   ```cmd
   cd YouTubePlaylistDownloader
   ```

3. Create a new virtual environment and activate it:

   ```cmd
   python -m venv <virtual-environment-name>
   <virtual-environment-name>\Scripts\activate
   ```

4. Install dependencies:

   ```cmd
   pip install -r requirements.txt
   ```

5. Run the application:

   ```cmd
   python .
   ```

## Parallelism and Concurrency

The YouTube Playlist Downloader utilizes thread-based parallelism for downloading videos concurrently. The `concurrent.futures.threadpoolexecutor` module is employed to manage and execute the download tasks efficiently.

## Performance Benchmarks

Before deciding on the module, Performance benchmarks were conducted on a playlist with 70 videos, each approximately 5 minutes long. The project initially used a couple of modules and techniques before deciding on the final approach, i.e. thread-based parallelism with asynchronous programming:

| Technique                                                                                   | Time taken (second) |
| ------------------------------------------------------------------------------------------- | ------------------- |
| Synchronous programming (normal)                                                            | 423                 |
| Thread-based parallelism (`Threading`)                                                      | 355                 |
| Multiprocessing (`multiprocessing`)                                                         | 360                 |
| Asynchronous programming (`asyncio`)                                                        | 354                 |
| Thread-based parallelism (`concurrent.futures`)                                             | 350                 |
| Thread-based parallelism with asynchronous programming (`concurrent.futures` and `asyncio`) | 333                 |

## Benchmark Observations

These observations showcase the iterative and experimental nature of optimizing the project, providing insights into the effectiveness of different parallelization techniques.

- Synchronous Approach:

  - Initially employed a synchronous approach for downloading videos.
  - Despite being time-consuming, the individual download times for videos were surprisingly shorter.

- Multiprocessing Exploration:

  - Tried `multiprocessing` to utilize all available cores for enhanced parallelism.
  - There were positive results; however, the overall improvement was somewhat mitigated by the overhead of creating new processes.
  - Moreover, `multiprocessing` proved less advantageous in scenarios involving significant I/O operations like downloading from the internet.

- Threading with `Threading` Module:

  - Tried threading using the `Threading` module.
  - Leveraged the lightweight nature of threads, which showcased a notable improvement in the overall download process.
  - There were times where the times were longer than that of `multiprocessing`. Reasons may range from inefficient use of network to Global Interpreter Lock (`GIL`).

- `AsyncIO` Experimentation:

  - Turned to `AsyncIO`, considering it is best suitable for I/O-bound operations.
  - There were promising results, yet the change in benchmarks was not quite impressive. However, I decided to keep this as an option.

- Discovery of `concurrent.futures`:

  - Accidentally stumbled upon `concurrent.futures` while researching other options, realizing its potential as a lightweight and efficient alternative.
  - Turns out `concurrent.futures` is more effective than traditional threading due to its bare-bones nature.
  - Decided to keep this as an option too, maybe even considering a hybrid approach.

- Combining `concurrent.futures` and `AsyncIO`:
  - Opted for a hybrid approach, combining the strengths of `concurrent.futures` and `AsyncIO`.
  - This achieved the most substantial improvement in download times.
  - The asynchronous, parallelized thread spawning resulted in a highly responsive and efficient download process.
  - While this may not be the optimal option, I decided to stick with this approach as it is better than other options I have tried.

## Architecture

The architecture involves a graphical user interface created with customtkinter. The parallel video download process is orchestrated using the `concurrent.futures.ThreadPoolExecutor`. Each video download task runs in a separate thread, ensuring efficient utilization of resources and faster downloads.

## Usage

1. Run the application using the setup instructions.
2. Input the YouTube playlist link in the provided entry box.
3. Click the "Download" button to initiate the parallel video download process.
4. Monitor the progress in the application.
5. Check the `Downloads` folder for the downloaded videos.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the functionality or fix any bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Conclusion

This was such a fun project to work with! I was fascinated by the concepts of concurrency and parallelism and this project really made me understand many things about them. By the way, Feel free to fork this project, customize, improve, and make it your own!

Feel free to connect with me on [LinkedIn](www.linkedin.com/in/khair-alanam) or [Twitter](https://twitter.com/khair_alanam). I would love to connect and discuss with you on everything related to tech :-)

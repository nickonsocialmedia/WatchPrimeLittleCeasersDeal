import subprocess
import platform


def open_chromium_with_android_agent():
    # Specify the command to launch Chromium with the Android user agent
    command = ""

    # Check the platform to determine the appropriate command
    if platform.system() == 'Linux':
        # Use the 'snap' command for Ubuntu (assuming Chromium is installed via Snap)
        command = "snap run chromium --user-agent=\"Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36\""
    elif platform.system() == 'Windows':
        # Add Windows command if needed
        pass
    elif platform.system() == 'Darwin':
        # Add macOS command if needed
        pass
    else:
        print("Unsupported operating system")
        return

    try:
        # Run the command to open Chromium with the specified user agent
        subprocess.run(command, shell=True)

        # Wait for user input before exiting
        input("Press Enter to exit...")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    open_chromium_with_android_agent()

import subprocess
import sys
from pathlib import Path


def main():
    print("Generating Protobuf files...")

    # this should be the utils folder
    SCRIPT_DIR = Path(__file__).resolve().parent

    # this is models dir
    MODELS_DIR = SCRIPT_DIR.parent

    PROTO_SRC_DIR = MODELS_DIR / "protos"
    PROTO_FILE = PROTO_SRC_DIR / "scribble_types.proto"
    OUTPUT_DIR = MODELS_DIR / "generated"

    command = [
        "python",
        "-m",
        "grpc_tools.protoc",
        f"-I={PROTO_SRC_DIR}",
        f"--python_out={OUTPUT_DIR}",
        f"--pyi_out={OUTPUT_DIR}",
        f"{PROTO_FILE}",
    ]

    result = subprocess.run(command)

    if result.returncode == 0:
        print("Protobuf files generated successfully!")
    else:
        print("Error: Protobuf generation failed.", file=sys.stderr)
        sys.exit(result.returncode)


if __name__ == "__main__":
    main()

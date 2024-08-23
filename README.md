# mmdetection-lars

This project involves adapting the mmdetection library to perform panoptic segmentation using the LaRS dataset. The mmdetection library originally does not support the LaRS dataset, so custom modifications were made to create a new dataloader and adjust the library to be compatible with LaRS for panoptic segmentation tasks.

## Features

- **Panoptic Segmentation:** Uses mmdetection's powerful panoptic segmentation capabilities.
- **LaRS Dataset Support:** Custom dataloader and adjustments to support the LaRS dataset.
- **Flexible and Extensible:** The project maintains the flexibility of mmdetection while extending its capabilities to new datasets.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- [Python 3.8+](https://www.python.org/)
- [PyTorch](https://pytorch.org/) (compatible version)
- [mmdetection](https://github.com/open-mmlab/mmdetection) (installed as per the official instructions)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sugihAF/mmdetection-lars.git
    ```
2. Navigate to the project directory:
    ```bash
    cd mmdetection-lars
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Setting Up LaRS Dataset

1. Ensure the LaRS dataset is properly formatted and located in the specified directory.
2. Modify the dataset path and configuration in the provided configuration files to point to your LaRS dataset.

### Running the Panoptic Segmentation

To start training or evaluation with the LaRS dataset:

1. Configure the model and dataset settings in the config files.
2. Run the training script:
    ```bash
    python tools/train.py configs/your_config_file.py
    ```
3. For evaluation:
    ```bash
    python tools/test.py configs/your_config_file.py checkpoints/your_checkpoint.pth
    ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code is well-documented and tested before submission.

## License

This project is licensed under the MIT License.

## Contact

For any questions or inquiries, feel free to reach out to the project maintainer [Sugih AF](https://github.com/sugihAF).

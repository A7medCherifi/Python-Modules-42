from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}\n"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid numeric data"
        total = len(data)
        sum_num = sum(data)
        avg_num = float(sum(data) / len(data))
        return f"Processed {total} numeric values,\
 sum={sum_num}, avg={avg_num:.1f}"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(x, int) for x in data)
        return isinstance(data, int)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid text data"
        total = len(data)
        words = data.split(' ')
        return f"Processed text: {total} characters, {len(words)} words"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid Log data"
        log = data.split(':', 1)
        alert = log[0].strip()
        discreption = log[1].strip() if len(log) > 1 else "Unknown"
        self.log_type = "[ALERT]" if alert == "ERROR" else "[INFO]"
        return f"{alert} level detected: {discreption}"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def format_output(self, result):
        txt = f"{self.log_type} {result}"
        return super().format_output(txt)


def stream_processor(obj, data):
    print(f"Processing data: {data}")
    print("Validation: ", end="")
    print("Numeric data verified" if obj.validate(data) else "Invalid data")
    output = obj.process(data)
    print(obj.format_output(output))


def process_all_data():
    print("=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")
    multiple_data = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "Slaack ajmi!"),
        (LogProcessor(), "INFO: System ready")
    ]

    for i, (processor, data) in enumerate(multiple_data, 1):
        result = processor.process(data)
        print(f"Result {i}: {result}")
    print("Foundation systems online. Nexus ready for advanced streams.")


def test_stream_processor():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    try:
        print("Initializing Numeric Processor...")
        num = NumericProcessor()
        data = [1, 2, 3, 4, 5]

        stream_processor(num, data)

        print("Initializing Text Processor...")
        text = TextProcessor()
        data = "Hello Nexus World"

        stream_processor(text, data)

        print("Initializing Log Processor...")
        log = LogProcessor()
        data = "ERROR: Connection timeout"
        stream_processor(log, data)

    except Exception as e:
        print(f"ERROR: {e}\n")
    process_all_data()


if __name__ == "__main__":
    test_stream_processor()

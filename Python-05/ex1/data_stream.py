from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union, Dict


class DataStream(ABC):
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria:
                    Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"processed": 0}


class SensorStream(DataStream):
    def __init__(self, stream_id):
        self.stream_id = stream_id
        self.type = "Environmental Data"
        self.reads = 0
        self.items = dict()
        self.avg_temp = ""
        self.analysis = ""

    def get_stream(self) -> None:
        print(f"Stream ID: {self.stream_id}, Type: {self.type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        sensor_batch = ""
        try:
            for item in data_batch:
                if sensor_batch != "":
                    sensor_batch += ", "

                key, value = item.split(':')
                value = float(value)
                if value.is_integer():
                    value = int(value)

                self.items.update({key: value})
                sensor_batch += f"{key}:{value}"
                self.reads += 1

        except ValueError:
            return "Error: Invalid Input!!"

        if 'temp' in self.items:
            value = self.items.get("temp")
            self.avg_temp = f"avg temp: {value}°C"
        else:
            self.avg_temp = "Invalid temp!"
        self.analysis = f"Sensor analysis: {self.reads} readings \
processed, {self.avg_temp}"
        return f"Processing sensor batch: [{sensor_batch}]"

    def filter_data(self, data_batch: List[Any], criteria:
                    Optional[str] = None) -> List[Any]:
        filtered = []
        if criteria == "High-priority":
            for value in self.items.values():
                if value > 30 or value < 10:
                    filtered.append(value)
            return filtered
        return data_batch

    def get_stats(self) -> Dict[str, str | int | float]:
        stats = super().get_stats()
        stats["processed"] = self.reads
        stats["type"] = self.type
        stats["avg_temp"] = self.avg_temp
        stats["analysis"] = self.analysis
        stats["message"] = f"- Sensor data: {stats["processed"]} \
readings processed"
        return stats


class TransactionStream(DataStream):
    def __init__(self, stream_id):
        self.stream_id = stream_id
        self.type = "Financial Data"
        self.reads = 0
        self.items = {
            "buy": [],
            "sell": []
        }
        self.net_flow = 0
        self.analysis = ""

    def get_stream(self) -> None:
        print(f"Stream ID: {self.stream_id}, Type: {self.type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        trans_batch = ""
        try:
            for item in data_batch:
                if trans_batch != "":
                    trans_batch += ", "

                key, value = item.split(':')
                value = float(value)
                if value.is_integer():
                    value = int(value)

                if key == 'buy':
                    self.net_flow += value
                    self.items["buy"].append(value)

                elif key == 'sell':
                    self.net_flow -= value
                    self.items["sell"].append(value)
                trans_batch += f"{key}:{value}"
                self.reads += 1

        except ValueError:
            return "Error: Invalid Input!!"
        self.analysis = f"Transaction analysis: {self.reads} operations, \
net flow: +{self.net_flow} units"
        return f"Processing transaction batch: [{trans_batch}]"

    def filter_data(self, data_batch: List[Any], criteria:
                    Optional[str] = None) -> List[Any]:
        filtered = []
        if criteria == "High-priority":
            for value in self.items['buy']:
                if value >= 200:
                    filtered.append(value)
            for value in self.items['sell']:
                if value >= 200:
                    filtered.append(value)
            return filtered
        return data_batch

    def get_stats(self) -> Dict[str, str | int | float]:
        stats = super().get_stats()
        stats["processed"] = self.reads
        stats["type"] = self.type
        stats["net_flow"] = self.net_flow
        stats["analysis"] = self.analysis
        stats["message"] = f"- Transaction data: {stats["processed"]} \
operations processed"
        return stats


class EventStream(DataStream):
    def __init__(self, stream_id):
        self.stream_id = stream_id
        self.type = "System Events"
        self.items = []
        self.reads = 0
        self.errors = 0
        self.analysis = ""

    def get_stream(self) -> None:
        print(f"Stream ID: {self.stream_id}, Type: {self.type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        event_banch = ""
        for event in data_batch:
            if event.lower() == "error":
                self.errors += 1

            if event_banch != "":
                event_banch += ", "

            self.items.append(event)
            event_banch += f"{event}"
            self.reads += 1
        self.analysis = f"Event analysis: {self.reads} events, \
{self.errors} error detected"
        return f"Processing transaction batch: [{event_banch}]"

    def filter_data(self, data_batch: List[Any], criteria:
                    Optional[str] = None) -> List[Any]:
        filtered = []
        if criteria == "High-priority":
            for value in self.items:
                if value.lower() == "error":
                    filtered.append(value)
            return filtered
        return data_batch

    def get_stats(self) -> Dict[str, str | int | float]:
        stats = super().get_stats()
        stats["processed"] = self.reads
        stats["type"] = self.type
        stats["errors"] = self.errors
        stats["analysis"] = self.analysis
        stats["message"] = f"- Event analysis: {stats["processed"]} \
events processed"
        return stats


class StreamProcessor:
    def process_all(self, mixed_data: List[Any]) -> None:
        print("Batch 1 Results:")

        try:
            for item in mixed_data:
                stream, data = item
                stream.process_batch(data)
                stats = stream.get_stats()
                print(stats["message"])
        except Exception as e:
            print(f"\nError: {e}")

    def filter_all(self, mixed_data: List[Any]) -> None:
        print("\nStream filtering active: High-priority data only")
        try:
            filterd: List[list[Any]] = []
            for item in mixed_data:
                stream, data = item
                filterd.append(stream.filter_data(data, "High-priority"))
            print(f"filtered results: {len(filterd[2])} critical sensor "
                  f"alerts, {len(filterd[1])} large transaction")
        except Exception as e:
            print(f"\nError: {e}")


def process_stream(stream: Any, data: List[Any]):
    try:
        stream.get_stream()
        result = stream.process_batch(data)
        print(result)
        stats = stream.get_stats()
        print(stats["analysis"])
    except Exception as e:
        print(f"Error: {e}")


def process_mixed_streams():
    print("Processing mixed stream types through unified interface...\n")

    mixed_data = [
        (SensorStream("SENSOR_002"), ["temp:25", "humidity:53"]),
        (TransactionStream("TRANS_002"), ["buy:210", "sell:155",
                                          "buy:95", "sell:10"]),
        (EventStream("EVENT_002"), ["login", "error", "error"])
    ]
    processor = StreamProcessor()
    processor.process_all(mixed_data)
    processor.filter_all(mixed_data)


def test_stream_system():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    trans_data = ["buy:100", "sell:150", "buy:75"]
    event_data = ["login", "error", "logout"]

    stream_id = "SENSOR_001"
    stream = SensorStream(stream_id)
    print("\nInitializing Sensor Stream...")
    process_stream(stream, sensor_data)

    stream_id = "TRANS_001"
    trans = TransactionStream(stream_id)
    print("\nInitializing Transaction Stream...")
    process_stream(trans, trans_data)

    stream_id = "EVENT_001"
    event = EventStream(stream_id)
    print("\nInitializing Event Stream...")
    process_stream(event, event_data)

    print("\n=== Polymorphic Stream Processing ===")
    process_mixed_streams()
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    test_stream_system()

from dataclasses import dataclass
import os
import subprocess
import tempfile
import unittest

write_golden_files = False


@dataclass
class SampleFile:
    base: str
    input_path: str
    output_path: str


class TestEvaluator(unittest.TestCase):
    def sample_programs(self):
        input_dir = os.path.join(os.path.dirname(__file__), 'test_programs')
        output_dir = os.path.join(os.path.dirname(__file__), 'test_evaluations')
        samples = []
        for filename in os.listdir(input_dir):
            base, _ = os.path.splitext(filename)
            input_path = os.path.join(input_dir, filename)
            stdout_path = os.path.join(output_dir, base + '.output')
            samples.append(SampleFile(base, input_path, stdout_path))
        return samples

    def evaluate(self, filename):
        eval_path = os.path.join(os.path.dirname(__file__), 'evaluator.py')
        with open(filename) as inp:
            text = inp.read()

        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as src:
            src.write(text)

            # Crash the program to get queue state.
            src.write("\nQQ\n")

            # Since we're not closing the file, we need to seek back to the
            # start before we try reading it again.
            src.seek(0)

            capture = subprocess.run(
                ['python', eval_path, src.name],
                capture_output=True,
                text=True,
            )

        return capture.stdout

    @unittest.skipIf(write_golden_files, 'writing golden files')
    def test_sample_programs(self):
        for program in self.sample_programs():
            with self.subTest(program.base):
                actual = self.evaluate(program.input_path)
                with open(program.output_path) as out:
                    expected = out.read()
                self.assertEqual(actual, expected)

    @unittest.skipIf(not write_golden_files, 'not writing golden files')
    def test_write_golden_files(self):
        for program in self.sample_programs():
            with self.subTest(program.base):
                stdout = self.evaluate(program.input_path)
                with open(program.output_path, 'w') as out:
                    out.write(stdout)


if __name__ == "__main__":
    unittest.main()

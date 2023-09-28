# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Integration code for quadfuzz fuzzer."""

from fuzzers.libfuzzer import fuzzer as libfuzzer

# Just reuse the libfuzzer class


def build():
    """Build benchmark."""
    libfuzzer.build()


def fuzz(input_corpus, output_corpus, target_binary):
    """Run fuzzer. Wrapper that uses the defaults when calling
    run_fuzzer."""
    libfuzzer.run_fuzzer(input_corpus,
                         output_corpus,
                         target_binary,
                         extra_flags=["-max_len=262144", "-timeout=30"])

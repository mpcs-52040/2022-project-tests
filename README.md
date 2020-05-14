# FINAL Tests
this are the unit test that will be used for grading your Final.


## Install pytest
you will need pytest for running these test.

```bash
> pip3 install pytest
```

## How to run
to run them you can copy the test folder in your repository and run from your root repository folder:
```bash
> pytest
```
pytest will run all file names starting or ending with `test`, as in `test_example.py` or `example_test.py`.

you can also run a specific file
```bash
> pytest 1_MQ_test.py
```

to create new test make sure that your function name starts with `test`

## Test Description

`test_utils.py` has some classes that will manage a node and a group of nodes called swarm. nodes and swarms can be started and stopped. nodes can receive requests with function like `get_message`, `put_message`.

`message_queue_test.py` will test your step 1 of the message queue implementation. all those tests are starting your node in an external process and its relative configuration. test will try to getting/putting messages and topics verifying the expected output.

## Notes

for any questions ask in slack `project-questions`

these test will be updated when there are new test releases and or bug fixes. for every update you will be notified on slack `announcements`

`@pytest.fixture` are the functions called by tests before running. in this case we use them to start the nodes, then terminate them when the test is done.

the test has a variable called `PROGRAM_FILE_PATH` that specifies where the `node.py` file is. you can change it for your tests but that is the place where the submission file should be. now is `"src/node.py"` because tests are meant to be run in the repository root folder.

`config.json` will be created in the root folder

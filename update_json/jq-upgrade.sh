#!/bin/bash

jq '.logs.logs_collected.files.collect_list += [{"file_paty": "two"}, {"file_path": "three"}]' data.json
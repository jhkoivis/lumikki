#!/bin/sh


killall ssh
ssh hugo.hut.fi killall ssh
ssh hugo.hut.fi ssh erin.hut.fi killall ssh


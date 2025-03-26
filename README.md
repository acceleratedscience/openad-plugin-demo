# OpenAD Demo Plugin

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/openad)](https://pypi.org/project/openad/)
[![License MIT](https://img.shields.io/github/license/acceleratedscience/open-ad-toolkit)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This is a demonstration plugin for OpenAD plugin developers.

You can use it as a scaffold to develop your own plugins, and to learn how to use a number of OpenAD tools in your own plugins, like visualizing molecules and other data.

<br>

## Install Plugin

```shell
pip install git+https://github.com/acceleratedscience/openad-plugin-demo
```

To see the plugin splash screen, simply run:

```shell
demo
```

To see how the plugin commands are now integated in the general OpenAD help:

```shell
?
```

<br>

## Build Your Own

First clone the plugin repo:

```shell
git clone --no-remote git@github.com:acceleratedscience/openad-plugin-demo.git
```

If you previously installed the GitHub version, first remove it:

```shell
pip uninstall openad-plugin-demo
```

Then install the downloaded repo with the `--editable` flag, so you can edit the plugin code:

```shell
cd openad-plugin-demo
```
```shell
pip install -e .
```

Duplicate the [commands/hello_world](openad_plugin_demo/commands/hello_world) directory as a scaffold for every command you build into your plugin.

Now relaunch openad every time you want to see an edit you made.

```shell
exit
```
```shell
openad
```

<br>

### Learning

The plugin code is relatively simple and self-explanatory.  
You'll find documentation across the code to help you along.

If you prefer a step-by-step guide on how to build your own plugin, head to the [Plugin Developer Guide](https://openad.accelerate.science/documentation/plugins/#creating-your-own-plugin).
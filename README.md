# OpenAD Demo Plugin

This is a demonstration plugin for OpenAD plugin developers.

You can use it as a scaffold to develop your own plugins, and learn how to use a number of OpenAD tools in your plugins, like visualizing molecules and other data.

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

First download the plugin:

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

Duplicate the [commands/hello_world] directory as a scaffold for every command you build into your plugin.

Now relaunch openad every time you want to see an edit you made.

```shell
exit
```
```shell
openad
```

To see a step-by-step guide on how to build your own plugin, head to the [Plugin Developer Guide](https://openad.accelerate.science/documentation/plugins/#creating-your-own-plugin).
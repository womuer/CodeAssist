const vscode = require('vscode');

function activate(context) {
    // 声明一个用于存储配置信息的数组
    let configurations = vscode.workspace.getConfiguration().get('myExtension.configurations', []);

    // 命令：打开配置页面
    let disposable = vscode.commands.registerCommand('extension.openConfigurationPage', () => {
        vscode.window.showInputBox({
            prompt: 'User snippets:',
        }).then(name => {
            if (name) {
                // 添加新的配置信息
                configurations.push({ name, prefix: '', body: '', description: '' });

                // 更新配置
                vscode.workspace.getConfiguration().update('myExtension.configurations', configurations, vscode.ConfigurationTarget.Global);
            }
        });
    });

    // 命令：查看和编辑配置信息
    let viewConfigurations = vscode.commands.registerCommand('extension.viewConfigurations', () => {
        vscode.window.showQuickPick(configurations.map(cfg => cfg.name), {
            placeHolder: 'Select a configuration to edit:'
        }).then(selectedName => {
            const selectedConfig = configurations.find(cfg => cfg.name === selectedName);
            if (selectedConfig) {
                // 弹出编辑框，允许用户编辑配置信息
                vscode.window.showInputBox({
                    value: selectedConfig.prefix,
                    prompt: 'Edit the configuration:',
                }).then(editedPrefix => {
                    if (editedPrefix !== undefined) {
                        selectedConfig.prefix = editedPrefix;
                        vscode.workspace.getConfiguration().update('myExtension.configurations', configurations, vscode.ConfigurationTarget.Global);
                    }
                });
            }
        });
    });

    context.subscriptions.push(disposable, viewConfigurations);
}
exports.activate = activate;

function deactivate() { }

module.exports = {
    activate,
    deactivate
};

#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const chalk = require('chalk');

const SCRIPT_DIR = __dirname;
const ROOT_DIR = path.dirname(SCRIPT_DIR);
const MARKETPLACE_DIR = path.join(ROOT_DIR, 'marketplace', 'skills');

function printUsage() {
    console.log('Usage: npm run install [skill-name]');
    console.log('');
    console.log('Options:');
    console.log('  skill-name    Install a specific skill');
    console.log('  --all         Install all available skills');
    console.log('  --list        List available skills');
    console.log('  --help        Show this help message');
}

function listSkills() {
    console.log(chalk.blue('Available skills:'));
    console.log('');

    if (!fs.existsSync(MARKETPLACE_DIR)) {
        console.log(chalk.yellow('No skills directory found'));
        return;
    }

    const skills = fs.readdirSync(MARKETPLACE_DIR, { withFileTypes: true })
        .filter(dirent => dirent.isDirectory())
        .map(dirent => dirent.name);

    if (skills.length === 0) {
        console.log(chalk.yellow('No skills found'));
        return;
    }

    skills.forEach(skillName => {
        const skillDoc = path.join(MARKETPLACE_DIR, skillName, 'SKILL.md');
        if (fs.existsSync(skillDoc)) {
            const content = fs.readFileSync(skillDoc, 'utf8');
            const firstLine = content.split('\n')[0];
            const description = firstLine.replace(/^#\s+/, '');
            console.log(`  ${chalk.green(skillName)} - ${description}`);
        } else {
            console.log(`  ${chalk.yellow(skillName)} - (no documentation)`);
        }
    });
}

function installSkill(skillName) {
    const skillDir = path.join(MARKETPLACE_DIR, skillName);

    if (!fs.existsSync(skillDir)) {
        console.log(chalk.red(`Error: Skill '${skillName}' not found`));
        console.log(chalk.yellow('Available skills:'));
        listSkills();
        return false;
    }

    const installScript = path.join(skillDir, 'install.sh');

    if (!fs.existsSync(installScript)) {
        console.log(chalk.red(`Error: No install script found for skill '${skillName}'`));
        return false;
    }

    console.log(chalk.blue(`Installing skill: ${skillName}`));

    try {
        const { spawnSync } = require('child_process');
        const result = spawnSync('bash', [installScript], {
            cwd: skillDir,
            stdio: 'inherit'
        });

        if (result.status === 0) {
            console.log(chalk.green(`✓ Successfully installed skill: ${skillName}`));
            return true;
        } else {
            console.log(chalk.red(`✗ Failed to install skill: ${skillName}`));
            return false;
        }
    } catch (error) {
        console.log(chalk.red(`✗ Error installing skill '${skillName}': ${error.message}`));
        return false;
    }
}

function installAllSkills() {
    console.log(chalk.blue('Installing all available skills...'));
    console.log('');

    if (!fs.existsSync(MARKETPLACE_DIR)) {
        console.log(chalk.red('Error: No skills directory found'));
        return;
    }

    const skills = fs.readdirSync(MARKETPLACE_DIR, { withFileTypes: true })
        .filter(dirent => dirent.isDirectory())
        .map(dirent => dirent.name);

    if (skills.length === 0) {
        console.log(chalk.yellow('No skills found'));
        return;
    }

    let installedCount = 0;
    let failedCount = 0;

    for (const skillName of skills) {
        if (installSkill(skillName)) {
            installedCount++;
        } else {
            failedCount++;
        }
        console.log('');
    }

    console.log(chalk.green('Installation summary:'));
    console.log(`  ${chalk.green(`✓ Successfully installed: ${installedCount}`)} skills`);
    if (failedCount > 0) {
        console.log(`  ${chalk.red(`✗ Failed to install: ${failedCount}`)} skills`);
    }
}

// Main script logic
const args = process.argv.slice(2);
const command = args[0];

switch (command) {
    case '--help':
    case '-h':
        printUsage();
        break;
    case '--list':
    case '-l':
        listSkills();
        break;
    case '--all':
    case '-a':
        installAllSkills();
        break;
    case undefined:
        console.log(chalk.yellow('No skill specified. Use --all to install all skills or --list to see available skills.'));
        console.log('');
        printUsage();
        break;
    default:
        installSkill(command);
        break;
}
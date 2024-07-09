import json
import os
import disnake

def load(path:str) -> dict:
    if not os.path.exists(path):
        return
    _data = json.loads(open(path, "r").read())
    return _data

def save(path:str, _data:dict) -> None:
    open(path, "w").write(json.dumps(_data))

def default_server_data(guild: disnake.Guild) -> dict:
    default_data = {
        'Guild Current Name': f'{guild.name}',
        'Guild History Names': {},
        'Guild Roles': [],
        'Guild Deleted Roles': [],
        'Members': [],
        'Members Count': len(guild.members),
        'Greeting': {
            'Enabled': False
        },
        'Leveling': {
            'Enabled': False
        },
        'Economy': {
            'Enabled': False
        },
        'Moderation': {
            'Enabled': False
        },
        'Auto Role': {
            'Enabled': False
        },
        'Ticket Tool': {
            'Enabled': False
        },
        'Voice Manager': {
            'Enabled': False
        }
    }
    for role in guild.roles:
        default_data['Guild Roles'].append(role.id)
    for member in guild.members:
        default_data['Members'].append(member.id)
    return default_data

def default_user_data(member: disnake.Member) -> dict:
    default_data = {
        'User Current Name': f'{member.name}',
        'User Current Display Name': f'{member.display_name}',
        'User History Names': {},
        'User History Display Names': {},
        'User Ban History': {},
        'Server Member': [],
        'Level': {},
        'Eco': {},
        'Warns': {}
    }
    return default_data

def servers_data() -> list:
    default_data = {
        'Servers List': [],
        'Archive Servers List': []
    }
    if not os.path.exists('server-dat.json'):
        open('server-dat.json', 'w').write(json.dumps(default_data))
        return [default_data['Servers List'], default_data['Archive Servers List']]
    else:
        serv_data = load('server-dat.json')
        for key in ['Servers List', 'Archive Servers List']:
            if key not in serv_data.keys():
                serv_data[key] = []
        return [serv_data['Servers List'], serv_data['Archive Servers List']]

def create_server_space(guild: disnake.Guild) -> None:
    servers, servers_archive = servers_data()
    os.mkdir(f'data/servers/{guild.id}')
    server_data = default_server_data(guild)
    save(f'data/servers/{guild.id}/server_data.json', server_data)
    servers.append(guild.id)
    save('server-dat.json', {'Servers List': servers, 'Archive Servers List': servers_archive})

def check_users_data(guild: disnake.Guild) -> None:
    for member in guild.members:
        if f'{member.id}.json' not in os.listdir('data/users'):
            user_data = default_user_data(member)
            user_data['Server Member'].append(guild.id)
            save(f'data/users/{member.id}.json', user_data)
        user_data = load(f'data/users/{member.id}.json')
        if guild.id not in user_data['Server Member'] and member in guild.members:
            user_data['Server Member'].append(guild.id)
            save(f'data/users/{member.id}.json', user_data)

def archive_server(guild: disnake.Guild) -> None:
    servers, servers_archive = servers_data()
    os.mkdir(f'data/server_archive/{guild.id}')
    os.replace(f'data/servers/{guild.id}/server_data.json', f'data/server_archive/{guild.id}/server_data.json')
    os.rmdir(f'data/servers/{guild.id}')
    servers.remove(guild.id)
    servers_archive.append(guild.id)
    save('server-dat.json', {'Servers List': servers, 'Archive Servers List': servers_archive})

def restore_server(guild: disnake.Guild) -> None:
    servers, servers_archive = servers_data()
    os.mkdir(f'data/servers/{guild.id}')
    os.replace(f'data/servers_archive/{guild.id}/server_data.json', f'data/servers/{guild.id}/server_data.json')
    os.rmdir(f'data/servers_archive/{guild.id}')
    servers_archive.remove(guild.id)
    servers.append(guild.id)
    save('server-dat.json', {'Servers List': servers, 'Archive Servers List': servers_archive})

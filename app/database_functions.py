from tables import session
from sqlalchemy import and_

# get

def get_user(session, name):
	user = session.query(tables.User).filter_by(name=name).first()
	return user

def get_user_devices(session, name):
	user = get_user(session, name)
	if user:
		devices = user.user_devices
		return devices
	return None

def get_user_scenarios(session, name):
	user = get_user(session, name)
	if user:
		scenarios = user.user_scenarios
		return scenarios
	return None

# put

def put_user(session, user_name, password):
	if not get_user(session, user_name):
		new_user = tables.User(name=user_name, password=password)
		session.add(new_user)
		session.commit()
		return True
	return False

def put_user_scenario(session, user_name, scenario_name, scenario_content):
	scenarios = get_user_scenarios(session, user_name)
	for scenario in scenarios:
		if scenario.name == scenario_name:
			return False
	new_scenario = tables.UserScenario(user_name=user_name, name=scenario_name, content=scenario_content)
	session.add(new_scenario)
	session.commit()
	return True

def put_user_device(session, user_name, device_name, device_type, device_settings):
	devices = get_user_devices(session, user_name)
	for device in devices:
		if device.name == device_name:
			return False
	new_device = tables.UserDevice(user_name=user_name, name=device_name, type=device_type, settings=device_settings)
	session.add(new_device)
	session.commit()
	return True

# delete

def delete_user(session, user_name):
	session.query(tables.User).filter_by(name=user_name).delete()

def delete_user_scenario(session, user_name, scenario_name):
	session.query(tables.UserScenario).filter(and_(
	UserScenario.user_name == user_name,
	UserScenario.name == scenario_name)).delete()

def delete_user_device(session, user_name, device_name, device_type):
	session.query(tables.UserDevice).filter(and_(
	UserDevice.user_name == user_name,
	UserDevice.name == device_name,
	UserDevice.type == device_type)).delete()
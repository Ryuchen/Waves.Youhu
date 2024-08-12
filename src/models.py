

class Weapon:

    # Basic Info
    weaponId: int
    weaponName: str
    weaponType: int
    weaponStarLevel: int
    weaponIcon: str
    weaponEffectName: str
    effectDescription: str

    def __init__(self, weaponId: int, weaponName: str, weaponType: int, weaponStarLevel: int,
                    weaponIcon: str, weaponEffectName: str, effectDescription: str):
        self.weaponId = weaponId
        self.weaponName = weaponName
        self.weaponType = weaponType
        self.weaponStarLevel = weaponStarLevel
        self.weaponIcon = weaponIcon
        self.weaponEffectName = weaponEffectName
        self.effectDescription = effectDescription

    def __str__(self):
        return f"[{self.weaponId}]::{self.weaponName}@{self.weaponStarLevel}"


class Phantom:

    # Basic Info
    class PhantomProp:
        phantomPropId: int
        name: str
        phantomId: int
        quality: int
        cost: int
        iconUrl: str
        skillDescription: str

    class FetterDetail:
        groupId: int
        name: str
        iconUrl: str
        num: int
        firstDescription: str
        secondDescription: str

    class MainProp:
        attributeName: str
        iconUrl: str
        attributeValue: str

    class SubProp:
        attributeName: str
        iconUrl: str
        attributeValue: str

    phantomProp: PhantomProp
    cost: int
    quality: int
    level: int
    fetterDetail: FetterDetail
    mainProps: list
    subProps: list

    def __init__(self, phantomPropId, name, phantomId, quality, cost, iconUrl, skillDescription):
        self.phantomPropId = phantomPropId
        self.name = name
        self.phantomId = phantomId
        self.quality = quality
        self.cost = cost
        self.iconUrl = iconUrl
        self.skillDescription = skillDescription

    def __str__(self):
        return f"[{self.phantomPropId}]::{self.name}@{self.phantomId}"


class WavesRole:
    """
    Waves.Youhu.Role
    """

    # Basic Info
    roleId: int
    level: int
    breach: int
    roleName: str
    roleIconUrl: str
    rolePicUrl: str
    starLevel: int
    attributeId: int
    attributeName: str
    weaponTypeId: int
    weaponTypeName: str
    acronym: str
    mapRoleId: str

    # Chain Info
    chain: list = []

    # Equip Info
    weapon: dict = {
        "weapon": Weapon,
        "level": int,
        "breach": int,
        "resonLevel": int
    }
    phantoms: list = []

    # Skill Info

    def __init__(self, roleId: int, level: int, breach: int,
                    roleName: str, roleIconUrl: str, rolePicUrl: str,
                    starLevel: int, attributeId: int, attributeName: str,
                    weaponTypeId: int, weaponTypeName: str, acronym: str, mapRoleId: str) -> None:
        self.roleId = roleId
        self.level = level
        self.breach = breach
        self.roleName = roleName
        self.roleIconUrl = roleIconUrl
        self.rolePicUrl = rolePicUrl
        self.starLevel = starLevel
        self.attributeId = attributeId
        self.attributeName = attributeName
        self.weaponTypeId = weaponTypeId
        self.weaponTypeName = weaponTypeName
        self.acronym = acronym
        if mapRoleId:
            self.mapRoleId = mapRoleId
        else:
            self.mapRoleId = ""

    def __str__(self):
        return f"[{self.roleId}]::{self.roleName}@{self.level}"

    def equipWeapon(self, weapon: Weapon, level: int, breach: int, resonLvel: int) -> None:
        self.weapon.update(
            {
                "weapon": weapon,
                "level:": level,
                "breach:": breach,
                "resonLevel": resonLvel
            }
        )

    def equipPhantom(self, phantom: Phantom, level: int, ) -> None:
        item
        self.phantoms.append(phantom)

    def detail(self):
        weapon = self.weapon.get("weapon")
        return (f"角色：[{self.roleId}]::{self.roleName}@{self.level} \n"
                f"武器: [{weapon.weaponId}]::{weapon.weaponName}@{weapon.weaponStarLevel}")
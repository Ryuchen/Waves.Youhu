class Role:
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

    def __str__(self) -> str:
        return f"ID: {self.roleId} @ 名称: {self.roleName} -> 等级: {self.level}"

    def __repr__(self) -> str:
        return f"ID: {self.roleId} @ 名称: {self.roleName} -> 等级: {self.level}"


class Chain:
    """
    Waves.Youhu.Chain
    """
    name: str
    order: int
    description: str
    iconUrl: str
    unlocked: bool

    def __init__(self, name: str, order: int, description: str, iconUrl: str, unlocked: bool) -> None:
        self.name = name
        self.order = order
        self.description = description
        self.iconUrl = iconUrl
        self.unlocked = unlocked

    def __str__(self) -> str:
        return f"顺序: {self.order} @ 名称: {self.name} -> 激活: {self.unlocked}"

    def __repr__(self) -> str:
        return f"顺序: {self.order} @ 名称: {self.name} -> 激活: {self.unlocked}"


class Skill:
    """
    Waves.Youhu.Skill
    """
    id: int
    type: str
    name: str
    description: str
    iconUrl: str

    def __init__(self, id: int, type: str, name: str, description: str, iconUrl: str) -> None:
        self.id = id
        self.type = type
        self.name = name
        self.description = description
        self.iconUrl = iconUrl

    def __str__(self) -> str:
        return f"ID: {self.id} @ 名称: {self.name} -> 类型: {self.type}"

    def __repr__(self) -> str:
        return f"ID: {self.id} @ 名称: {self.name} -> 类型: {self.type}"


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
        return f"ID: {self.weaponId} @ 名称: {self.weaponName} -> 等级: {self.weaponStarLevel}"

    def __repr__(self) -> str:
        return f"ID: {self.weaponId} @ 名称: {self.weaponName} -> 等级: {self.weaponStarLevel}"


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

        def __init__(self, phantomPropId: int, name: str, phantomId: int, quality: int, cost: int, iconUrl: str, skillDescription: str) -> None:
            self.phantomPropId = phantomPropId
            self.name = name
            self.phantomId = phantomId
            self.quality = quality
            self.cost = cost
            self.iconUrl = iconUrl
            self.skillDescription = skillDescription

        def __str__(self) -> str:
            return f"ID: {self.phantomId} @ 名称: {self.name} -> Cost: {self.cost}"

        def __repr__(self) -> str:
            return f"ID: {self.phantomId} @ 名称: {self.name} -> Cost: {self.cost}"

    class FetterDetail:
        groupId: int
        name: str
        iconUrl: str
        num: int
        firstDescription: str
        secondDescription: str

        def __init__(self, groupId: int, name: str, iconUrl: str, num: int, firstDescription: str, secondDescription: str):
            self.groupId = groupId
            self.name = name
            self.iconUrl = iconUrl
            self.num = num
            self.firstDescription = firstDescription
            self.secondDescription = secondDescription

    class MainProp:
        attributeName: str
        iconUrl: str
        attributeValue: str

        def __init__(self, attributeName: str, iconUrl: str, attributeValue: str) -> None:
            self.attributeName = attributeName
            self.iconUrl = iconUrl
            self.attributeValue = attributeValue

        def __str__(self) -> str:
            return f"{self.attributeName}: {self.attributeValue}"

        def __repr__(self) -> str:
            return f"{self.attributeName}: {self.attributeValue}"

    class SubProp:
        attributeName: str
        iconUrl: str
        attributeValue: str

        def __init__(self, attributeName: str, iconUrl: str, attributeValue: str) -> None:
            self.attributeName = attributeName
            self.iconUrl = iconUrl
            self.attributeValue = attributeValue

        def __str__(self) -> str:
            return f"{self.attributeName}: {self.attributeValue}"

        def __repr__(self) -> str:
            return f"{self.attributeName}: {self.attributeValue}"

    phantomProp: PhantomProp
    cost: int
    quality: int
    level: int
    fetterDetail: FetterDetail
    mainProps: list[MainProp]
    subProps: list[SubProp]

    def __init__(self, phantomProp: dict, cost: int, quality: int, level: int, fetterDetail: dict, mainProps: list, subProps: list) -> None:
        self.phantomProp = self.PhantomProp(**phantomProp)
        self.cost = cost
        self.quality = quality
        self.level = level
        self.fetterDetail = self.FetterDetail(**fetterDetail)
        self.mainProps = [self.MainProp(**_) for _ in mainProps]
        self.subProps = [self.SubProp(**_) for _ in subProps]

    def __str__(self):
        return f"基础: {self.phantomProp} @ 主属性: {self.mainProps} -> 副词条: {self.subProps}"

    def __repr__(self):
        return f"基础: {self.phantomProp} @ 主属性: {self.mainProps} -> 副词条: {self.subProps}"

class WavesRole:
    """
    Waves.Youhu.Role
    """
    # Basic Info
    role: Role

    # Level Info
    level: int

    # Chains Info
    chainList: list[Chain]

    # Skills Info
    # [{ "skill": Skill, "level": int }]
    skillList: list[dict]

    # Equip Weapon Info
    weaponData: dict = {
        "weapon": Weapon,
        "level": int,
        "breach": int,
        "resonLevel": int
    }

    # Equip Phantom Info
    phantomData: dict = {
        "cost": int,
        "equipPhantomList": list[Phantom]
    }


    def __init__(self, role: dict) -> None:
        self.role = Role(**role)

    def __str__(self):
        return f"[{self.role.roleId}]::{self.role.roleName}@{self.level}"

    def level(self, level: int) -> None:
        self.level = level

    def setChainList(self, chainList: list) -> None:
        self.chainList = [Chain(**_) for _ in chainList]

    def setSkillList(self, skillList: list) -> None:
        self.skillList = [{"skill": Skill(**_["skill"]), "level": _["level"]} for _ in skillList]

    def equipWeapon(self, weaponData):
        self.weaponData["weapon"] = Weapon(**weaponData["weapon"])
        self.weaponData["level"] = weaponData["level"]
        self.weaponData["breach"] = weaponData["breach"]
        self.weaponData["resonLevel"] = weaponData["resonLevel"]

    def equipPhantom(self, phantomData):
        self.phantomData["cost"] = phantomData["cost"]
        self.phantomData["equipPhantomList"] = [
            Phantom(**_) for _ in phantomData["equipPhantomList"]
        ]

    def detail(self):
        print(f"角色：{self.role} \n")
        print(f"命座：{self.chainList} \n")
        print(f"技能：{self.skillList} \n")
        print(f"武器：{self.weaponData} \n")
        print(f"声骸：{self.phantomData} \n")
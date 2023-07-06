def old_function(train_type: int):
    if train_type == TrainType.IC:
        return TrafficType.DB_FERN
    elif train_type == TrainType.ICE:
        return TrafficType.DB_FERN
    elif train_type == TrainType.NACHTZUG:
        return TrafficType.OTHER
    elif train_type == TrainType.THALYS:
        return TrafficType.OTHER
    elif train_type == TrainType.DRITTE_FERNVERKEHR:
        return TrafficType.OTHER
    elif train_type == TrainType.REGIONALEXPRESS:
        return TrafficType.DB_REGIO
    elif train_type == TrainType.REGIONALBAHN:
        return TrafficType.DB_REGIO
    elif train_type == TrainType.SBAHN:
        return TrafficType.DB_SBAHN_WS
    elif train_type == TrainType.DRITTE_NAHVERKEHR:
        return TrafficType.OTHER
    elif train_type == TrainType.EINZELWAGEN_FERNVERKEHR:
        return TrafficType.DB_CARGO
    elif train_type == TrainType.EINZELWAGEN_NAHVERKEHR:
        return TrafficType.DB_CARGO
    elif train_type == TrainType.GANZZUG:
        return TrafficType.DB_CARGO
    elif train_type == TrainType.KOMBINIERTER_VERKEHR:
        return TrafficType.DB_CARGO
    elif train_type == TrainType.DRITTE_GUETERVERKEHR:
        return TrafficType.OTHER
    elif train_type == TrainType.LEERZUG:
        return TrafficType.OTHER
    elif train_type == TrainType.SCHADZUG:
        return TrafficType.OTHER
    else:
        raise ValueError("invalid train_type.")
    
def new_function(train_type: int) -> str:
    train_traffic_map = {
        TrainType.IC: TrafficType.DB_FERN,
        TrainType.ICE: TrafficType.DB_FERN,
        TrainType.NACHTZUG: TrafficType.OTHER,
        TrainType.THALYS: TrafficType.OTHER,
        TrainType.DRITTE_FERNVERKEHR: TrafficType.OTHER,
        TrainType.REGIONALEXPRESS: TrafficType.DB_REGIO,
        TrainType.REGIONALBAHN: TrafficType.DB_REGIO,
        TrainType.SBAHN: TrafficType.DB_SBAHN_WS,
        TrainType.DRITTE_NAHVERKEHR: TrafficType.OTHER,
        TrainType.EINZELWAGEN_FERNVERKEHR: TrafficType.DB_CARGO,
        TrainType.EINZELWAGEN_NAHVERKEHR: TrafficType.DB_CARGO,
        TrainType.GANZZUG: TrafficType.DB_CARGO,
        TrainType.KOMBINIERTER_VERKEHR: TrafficType.DB_CARGO,
        TrainType.DRITTE_GUETERVERKEHR: TrafficType.OTHER,
        TrainType.LEERZUG: TrafficType.OTHER,
        TrainType.SCHADZUG: TrafficType.OTHER
    }
    
    if train_type in train_traffic_map:
        return train_traffic_map[train_type]
    else:
        raise ValueError("invalid train_type.")
